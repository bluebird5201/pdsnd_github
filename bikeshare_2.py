import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New york city': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city =input ('please choose  a city (Chicago,New_york_city,Washington) :').title()
    while city not in ['Chicago','New_york_city','Washington']:
        city = input('please enter the valid value(Chicago,New_york_city,Washington) :').title()

    choose_time  = input('Do you want choose month and day? (yes or no) :')

    if choose_time=='yes'or choose_time=='Yes':
        # get user input for month (all, january, february, ... , june)
        month=input('please enter the month from the list(January, February, March, April, May, June) :').title()
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        while month not in months:
            month = input("please enter valid month from the list(January, February, March, April, May, June):").title()

        # get user input for day of week (all, monday, tuesday, ... sunday)
        day=input('please enter the day (eg, Monday...) :').title()
        days_of_week=['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday','Sunday']

        while day not in days_of_week:
            day = input("please enter valid days_of_week :").title()

    else:
        month=None
        day=None

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    '''
	load data  and get month and day from the string of data 
	and change string it to time 
	'''
    df=pd.read_csv(CITY_DATA[city])

    df['Start Time']=pd.to_datetime(df['Start Time'])
    #print(df['Start Time'].head())
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.weekday_name


    if month is not None:
        months=['January', 'February', 'March', 'April', 'May', 'June']
        month=months.index(month)+1
    #print(month)
        df = df[df['month'] == month]


    if day is not None:
     df=df[df['day']==day.title()]
    # print(df.head())
    return df
def display_data_function (df):
    while True:
        raw_data = input('Enter "5" for five lines.Enter "all" for whole data?')
        answer_list=['5','all','All']
        while raw_data not in answer_list :
            raw_data = input('please enter valide value ! Enter "5" for five lines.Enter "all" for whole data?')
        if raw_data=='5':
            print(df.head())
        else:
            print(df)

        relook = input('\nWould you like to take a look again? Enter yes or no.\n')

        if relook.lower() != 'yes':
            break

def time_stats_popule_month_day(df):
    
    print('The following statistice information do not filter by month and day of the week')
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('\nthe most common month:', popular_month)
    # display the most common day of week
    popular_day = df['day'].mode()[0]
    print('\nthe most common day of week :', popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    # print( df['hour'])
    print('\nthe most common start hour :', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def time_stats(df):
    
    print('The following statistice information filter by month and day of the week')
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

 

    # display the most common start hour
    df['hour']  = df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    #print( df['hour'])
    print('\nthe most common start hour :', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    #print( df['Start Station'])
    print('most commonly used start station : ',popular_start_station)
    #start_count = df['Start Station'].value_counts()
    #print(start_count)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('most commonly used end station : ',popular_end_station)

    # display most frequent combination of start station and end station trip
    df['combination_station']=df['Start Station']+df['End Station']
    #print('combination of start station and end station trip\n',df['combination_station'].head())
    popular_combination_station = df['combination_station'].mode()[0]
    print('most frequent combination of start station and end station trip : ', popular_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('total trip duration :',total_travel_time)

    # display mean travel time
    total_travel_time = df['Trip Duration'].mean()
    print('mean travel time :', total_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats_nogender(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display earliest, most recent, and most common year of birth
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    Gender = df['Gender'].value_counts()

    print(Gender)

    # Display earliest, most recent, and most common year of birth
    earliest_birth=df['Birth Year'].max()
    most_recent_birth=df['Birth Year'].min()
    most_common_year_birth=df['Birth Year'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        look_raw_data = input('Do you want to take a look raw data ? (yes or no)').title()
        if look_raw_data=='Yes':
            display_data_function(df)

        if month is None:
            time_stats_popule_month_day(df)
        else:
            time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city=='Washington':
            user_stats_nogender(df)
        else:
            user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
