import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
      
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter a city (Chicago, New York City, Washington)').strip().lower()
    while city not in CITY_DATA:
        print('invalid inputs!')
        city = input('enter city (Chicago, New York City, Washington)').strip().lower()
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    month = input('enter month from january to june:').strip().capitalize()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter day of the week:').strip().capitalize()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['day'] = df['Start Time'].dt.day_name()
    
    df['month'] = df['Start Time'].dt.month_name()
    if month != 'All':
        df=df[df['month']==month.title()]
    if day != 'All':
        df = df[df['day'] == day]
   
   
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(df['month'].head())
    common_month = df['month'].mode()[0]
    print('the most common month:', common_month)
    
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    common_day = df['day'].mode()[0]
    print('the most common day:', common_day)
    
   
    # TO DO: display the most common start hour
    df['hour']= df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('the most common hour', common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('the most commonly start station:' , most_common_start_station)
    
    # TO DO: display most commonly used end station
    df['End Station'] = df['End Station']
    most_common_end_station = df['End Station'].mode()[0]
    print('the most commonly used end station:', most_common_end_station)
    


    # TO DO: display most frequent combination of start station and end station trip
    df['combination station'] = df['Start Station'] + df['End Station']
    most_common_start_end_station = df['combination station'].mode()[0]
    print("The most commonly used start station and end station:",most_common_start_end_station) 
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('total_travel', total_travel)
   
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time:", mean_travel)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print("Counts of user type:", user_counts) 
     
    # TO DO: Display counts of gender
    
    
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print("Counts of gender:", gender_counts)
        
    # TO DO: Display earliest, most recent, and most common year of birth
        
        most_common_year = df['Birth Year'] .value_counts().mode()[0]
        most_recent = df['Birth Year'] .max()
        earliest_year = df['Birth Year'] .min()
        
        print("The most common birth year:", most_common_year)
        print("The most recent birth:", most_recent)
        print("The most earliest birth year:", earliest_year)
    else:     
        print("gender and birth year are unknown")


    
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        n=5
        raw_data = input ('would you like to display raw data? enter yes or stop: ').lower()
        while raw_data == 'yes': 
            print(df.head(n))
            n+=5
            raw_data = input ('would you like to display raw data? enter yes or stop: ').lower()
            if raw_data == 'yes': 
                print(df.head(n))
                n+=5
            elif raw_data == 'stop':
                break
                
                
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	 main()
