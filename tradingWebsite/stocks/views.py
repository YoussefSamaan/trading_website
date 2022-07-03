# django modules
from django.shortcuts import redirect, render
from django.contrib import messages

# local modules
from .login_required import login_required
from .stock_info import get_current_stock_price

# models
from .models import Portfolio, Stock

# accounts
from accounts.loggedin_restriction import loggedin_restriction


@loggedin_restriction
def front_page(request):
    return render(request, 'stocks/frontpage.html')


@login_required
def dashboard(request):

    portfolio = Portfolio.objects.get(user=request.user)
    stocks = Stock.objects.all().filter(portfolio=portfolio)
    prices = []
    portfolio_worth = portfolio.money_left

    for stock in stocks:
        stock_price = get_current_stock_price(stock)
        prices.append(stock_price)
        portfolio_worth += (stock_price * stock.shares)

    context = {
        'stocks_and_prices': zip(stocks, prices),
        'user': portfolio.user,
        'money_left': portfolio.money_left,
        'portfolio_worth': portfolio_worth,
    }

    return render(request, 'stocks/dashboard.html', context)


@login_required
def buy(request):
    if request.method == "POST":

        stock = request.POST['name']
        shares = int(request.POST['shares'])

        stock_price = get_current_stock_price(stock)
        if stock_price <= 0:
            messages.error(request, "This Stock is not available")
            return redirect("dashboard")

        user_porfolio = Portfolio.objects.get(user=request.user)
        user_porfolio_money_left = user_porfolio.money_left
        total_price_of_stocks = shares * stock_price

        if user_porfolio_money_left >= total_price_of_stocks:
            user_porfolio.money_left -= total_price_of_stocks
            user_porfolio.save()
            if not Stock.objects.filter(name=stock, portfolio=user_porfolio).exists():
                new_stock = Stock(name=stock, shares=shares,
                                  portfolio=user_porfolio)
                new_stock.save()
            else:
                stock_from_user = Stock.objects.get(
                    name=stock, portfolio=user_porfolio)
                stock_from_user.shares += shares
                stock_from_user.save()
            messages.success(request, "Transaction done")
            return redirect("dashboard")
        else:
            messages.error(
                request, "you do not have enough money to buy that manay shares")
            return redirect("dashboard")
    else:
        return render(request, 'stocks/404.html')


@login_required
def sell(request):
    if request.method == "POST":

        stock = request.POST['name']
        shares = int(request.POST['shares'])

        user_porfolio = Portfolio.objects.get(user=request.user)

        stock_price = get_current_stock_price(stock)
        if stock_price <= 0:
            messages.error(request, "This Stock is not available")
            return redirect("dashboard")

        if Stock.objects.filter(name=stock, portfolio=user_porfolio).exists():

            user_stock = Stock.objects.get(
                name=stock, portfolio=user_porfolio)

            if shares < user_stock.shares:
                total_price_of_stocks = shares * stock_price
                user_porfolio.money_left += total_price_of_stocks
                user_porfolio.save()
                user_stock.shares -= shares
                user_stock.save()
                messages.success(request, "Transaction done")
                return redirect("dashboard")
            elif shares == user_stock.shares:
                stock_price = get_current_stock_price(stock)
                total_price_of_stocks = shares * stock_price
                user_porfolio.money_left += total_price_of_stocks
                user_porfolio.save()
                user_stock.delete()
                messages.success(request, "transaction done")
                return redirect("dashboard")
            else:
                messages.error(request, "you do not have enough shares")
                return redirect("dashboard")
        else:
            messages.error(request, "you do not have this stock to sell it")
            return redirect("dashboard")

    else:
        return render(request, 'stocks/404.html')
