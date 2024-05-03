import matplotlib.pyplot as plt
import pandas as pd
import random

class Instrument:
    """
    Base class for financial instruments, with min and max percentage change
    and current price tracking.
    """
    def __init__(self, name, purchase_price, min_pct_change = -0.05, max_pct_change = 0.05):
        self.name = name
        self.purchase_price = purchase_price
        self.current_price = purchase_price
        self.min_pct_change = min_pct_change
        self.max_pct_change = max_pct_change

    def simulate_price_change(self):
        """
        Simulate a random price change for the instrument based on min and max percentage change.
        """
        pct_change = random.uniform(self.min_pct_change, self.max_pct_change)
        self.current_price += self.current_price * pct_change
        return self.current_price
    
    def report(self):
        """Generates a report of the instrument."""
        return f"Purchase price was {self.purchase_price}. Current price is {self.current_price}"


class Stock(Instrument):
    """
    Class representing a stock, inheriting from Instrument.
    """
    def simulate_return(self, current_date = None):
        """
        Simulate the daily return on investment for the stock by changing the current price.
        """
        return self.simulate_price_change()

class Bond(Instrument):
    """
    Class representing a bond, inheriting from Instrument, with coupon and coupon date.
    """
    def __init__(self, name, purchase_price, min_pct_change, max_pct_change, coupon, coupon_date):
        super().__init__(name, purchase_price, min_pct_change, max_pct_change)
        self.coupon = coupon
        self.coupon_date = coupon_date

    def simulate_return(self, current_date):
        """
        Simulate the daily return on investment for the bond by changing the current price and adding coupon if applicable.
        """
        new_price = self.simulate_price_change()
        if current_date == self.coupon_date:
            new_price += self.coupon
        return new_price

class Account:
    """
    Class representing a user's investment account, with added plotting functionality.
    """
    def __init__(self, user_name):
        self.user_name = user_name
        self.instruments = []
        self.movements = pd.DataFrame(columns=['Date', 'Instrument', 'Price'])
        self.date = 0

    def __str__(self):
        """
        Overrides the string method to print a summary of current prices of instruments in the account.
        """
        output_lines = [f"{self.user_name}'s Account:"]
        
        for instrument in self.instruments:
            output_lines.append(f"{instrument.name}: {instrument.report()}")
        
        return "\n".join(output_lines)

    def add_instrument(self, instrument):
        """
        Add a new financial instrument to the account.
        """
        self.instruments.append(instrument)

    def simulate_day(self):
        """
        Process daily movements, simulate returns for instruments, and update the account accordingly.
        """
        self.date += 1
        for instrument in self.instruments:
            new_price = instrument.simulate_return(self.date)
            new_row = pd.DataFrame({'Date': [self.date], 
                                    'Instrument': [instrument.name], 
                                    'Price': [new_price]})
            self.movements = pd.concat([self.movements, new_row], ignore_index=True)
            
    def simulate_n_days(self, number_of_days):
        """
        Simulates the passing of a specified number of days, applying daily simulations for each instrument in the account.        
        
        Args:
            number_of_days (int): The number of days to simulate.
        """
        for i in range(number_of_days):
            self.simulate_day()

    def plot_account_instruments(self):
        """
        Plots the price evolution of all instruments in the account over time.
        """
        plt.figure(figsize=(14, 8))
    
        # Loop through each instrument and plot its price over time
        for instrument in self.instruments:
            # Filter the movements DataFrame for the current instrument
            instrument_movements = self.movements[self.movements['Instrument'] == instrument.name]
    
            # Plot the instrument's price over time
            plt.plot(instrument_movements['Date'], instrument_movements['Price'], label=instrument.name, marker='o')
    
        plt.xlabel('Time (Days)')
        plt.ylabel('Price')
        plt.title(f'Price Evolution of Instruments in {self.user_name}\'s Account')
        plt.legend()
        plt.grid(True)
        plt.show()




#%%

mi_cuenta = Account('Facundo Kuzis')

accion_aapl = Stock(name = 'AAPL',
                    purchase_price = 1,
                    min_pct_change = -0.04,
                    max_pct_change = 0.04)

bono_bonito= Bond(name = 'Bonito',
                 purchase_price = 1,
                 min_pct_change = -0.02,
                 max_pct_change = 0.02,
                 coupon = 0.07,
                 coupon_date = 5)

mi_cuenta.add_instrument(accion_aapl)
mi_cuenta.add_instrument(bono_bonito)


#%%
mi_cuenta.simulate_n_days(20)

print(mi_cuenta)

#%% 
mi_cuenta.plot_account_instruments()
