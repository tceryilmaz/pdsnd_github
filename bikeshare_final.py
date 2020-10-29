import time
import pandas as pd
import numpy as np

CITY_DATA = { 'c': 'chicago.csv',
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

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Hello! Let\'s explore some US bikeshare data!')
    city = input("Please enter the name of the city to analyze; Chicago, new york city, washington:\n").lower()
    while city not in CITY_DATA.keys():
        city = input("This input is not recognized.\nPlease reenter the name of the city to analyze; chicago, new york city, washington:\n").lower()
    print('Thanks for the entry: \nWe will Analyze: ', city)


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please enter the month you want to analyze; Jan, Feb, Mar, Apr, May, Jun or all:\n").lower()
    while month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        if month in ('july', 'august', 'september', 'october', 'november', 'december'):
            print('Our data covers only the months from January to June.\nPlease choose a month accordingly.\n')
        else:
            print("Input not recognized.\n")
        month = input("Please reenter the month you want to analyze;\n January,\n February,\n March,\n April,\n May,\n June\n or all:\n").lower()
    print('Thanks for the entry: We will analyze', city, 'for ', month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter the day of the week; Monday, Tuesday, ... Sunday or all:\n").lower()
    while day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
        day = input("Day not recognized.\nPlease reenter the day you want to analyze;\n Monday,\n Tuesday,\n Wednesday,\n Thursday,\n Friday,\n Saturday,\n Sunday or all:\n").lower()
    if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
        print('Thanks for the entry: \nWe will analyze', city, 'for each ', day, 'in ',month)
    else:
        print('Thanks for the entry: \nWe will analyze', city, 'for ', month, 'without any day filter.')

    print('-'*40)
    print(city, month, day)
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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df['city2'] = city
    popular_month = df['month'].mode()[0]#calculates the most popular month regardless of the chosen month.
    df['month2'] = popular_month
    popular_day = df['day_of_week'].mode()[0]
    df['day2'] = popular_day
    popular_hour = df['hour'].mode()[0]
    df['hour2'] = popular_hour
    df['trip'] = ('from ') + df['Start Station'] + (' to ') + df['End Station']
    #popular_day2 = popular_day
    #df['day3'] = popular_day2
    print('Out of 6 months of data, regardless of any month or day filter;')
    print('for ', city, ':')
    print('most common month is:           ',popular_month)
    print('most common day of the week is: ',popular_day)
    print('most common hour is:            ',popular_hour)
    #print('Remember, the chosen day is:', day)
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]


    if day != 'all':
        # filter by day of week to create the new dataframe
        #daysall = ['Monday', 'Tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        #day_index = daysall.index(day) + 1
        df = df[df['day_of_week'] == day.capitalize()]
        return df

    #df = df[df['day_of_week'] == day]
    #df['trip'] = df.str.join(df['Start Station'], df[End Station])
    #popular_day2 = df['day_of_week'].mode()[0]#recalculates the day for the chosen month
    #df['day3'] = popular_day2
    #popular_day3 = df['day_of_week'].mode()[0]
    #df['day4'] = popular_day3
    return df
    #return popular_month #şimdilik bir işe yaramıyor!


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #print('most common month for',city,' is: ',popular_month)
    #print('most common month for ', df.iloc[1,12], 'is: ', df.iloc[1,13])
    # TO DO: display the most common day of week
    #popular_day3 = df['day_of_week'].mode()[0]
    print('The most common day of the week in ', df.iloc[1,12], 'over 6 months period is: ', df.iloc[1,14])
    print('However, for this specific month, the most common day of the week is: , popular_day3')
    popular_hour2 = df['hour'].mode()[0]

    print('The most common start hour is: ', popular_hour2)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip for the chosen month and days...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ', popular_start)


    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('And the most commonly used end station is: ', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = df['trip'].mode()[0]
    print('The most popular trip is', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time_total = df['Trip Duration'].sum()
    print('Total travel time is ',travel_time_total, 'seconds. That is: \n')
    travel_year = travel_time_total // (60*60*24*30*12)
    travel_month = (travel_time_total // (60*60*24*30)) - (travel_year * 12)
    travel_day = (travel_time_total // (60*60*24)) - ((travel_year * 12)+ travel_month)*30
    travel_hour = (travel_time_total // (60*60)) - (((travel_year * 12)+ travel_month) * 30 + travel_day)*24
    travel_minute = (travel_time_total // 60) - (((((travel_year * 12)+ travel_month)*30)+travel_day)*24 + travel_hour) * 60
    travel_second = travel_time_total % (60)
    print(travel_year, 'years,\n', travel_month, 'months\n', travel_day, 'days,\n', travel_hour, 'hours,\n', travel_minute, 'minutes,\n', travel_second, 'seconds,\n')
    # TO DO: display mean travel time
    event_count = df['Trip Duration'].count()

    mean_travel_time = travel_time_total // event_count
    print('Mean travel time is: ',mean_travel_time, 'seconds')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('TOTAL # of EVENTS:', event_count)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The user types are as follows: ')
    print(user_types)
    print('-*'*40)
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_types = df['Gender'].value_counts()
        print('The Gender distribution of users are as follows: ')
        print(gender_types)
        print('-*'*40)
    else:
        print('No Gender information for this city')
    print('-'*40)
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('Birth Year stats are as follows')
        oldest_birthyear = df['Birth Year'].min()
        print('The earliest Birth year is: ', oldest_birthyear)
        newest_birthyear = df['Birth Year'].max()
        print('The most recent Birth year is: ', newest_birthyear)
        common_birthyear = df['Birth Year'].mode()[0]
        print('The most common Birth year is: ', common_birthyear)
        print('-*'*40)
        print("\nThis took %s seconds." % (time.time() - start_time))
    else:
        print('No Birth Year information for this city')
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    print('-*'*40)
    #for col in df.columns:
    #    print(col)
    #print('-*'*40)
    #print(df.iloc[0:5, 0:6])
    #print('--->  '*5)
    #print(df.iloc[0:5, 6:12])
    #print('--->  '*5)
    #print(df.iloc[0:5, 12:17])
    #print('--->  '*5)
    showrows = 1
    while showrows > 0:
        print('sampling rows from',showrows, ' to', showrows + 4, ':\n',df.iloc[(showrows-1):(showrows + 4)])
        showmore = input('\nWould you like to see more? Enter y to see more or any other key to terminate.\n')
        if showmore in ('yes'):
            showrows += 5
        else:
            break


if __name__ == "__main__":
	main()
