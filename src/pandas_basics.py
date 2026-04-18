"""
Pandas Basics for GIS Data Analysis - Student Implementation

Complete the four functions in this file.
Use the notebooks to learn and test each function.

📋 FUNCTIONS TO IMPLEMENT IN THIS FILE:
=====================================
✅ Function 1: load_and_explore_gis_data()     → notebooks/01_function_...
✅ Function 2: filter_environmental_data()     → notebooks/02_function_...
✅ Function 3: calculate_station_statistics()  → notebooks/03_function_...
✅ Function 4: join_station_data()             → notebooks/04_function_...
"""

import pandas as pd
from pathlib import Path
import os


# =============================================================================
# FUNCTION 1: LOAD AND EXPLORE GIS DATA
# =============================================================================

def load_and_explore_gis_data(file_path):
    """
    Load a CSV file and display comprehensive information about the dataset.

    This function demonstrates the first step in any data analysis project:
    understanding your data through exploration.

    Args:
        file_path (str): Path to the CSV file to load

    Returns:
        pandas.DataFrame: The loaded dataset, or None if loading failed

    Example:
        >>> stations_df = load_and_explore_gis_data('data/weather_stations.csv')
        Loading data from: data/weather_stations.csv
        Dataset shape: (150, 6) - That's 150 rows and 6 columns!
        ...
    """

    print("=" * 50)
    print("LOADING AND EXPLORING GIS DATA")
    print("=" * 50)

    print(f"Loading data from: {file_path}")

    # Try to load the CSV file
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"ERROR: File not found: {file_path}")
        return None
    except Exception as e:
        print(f"ERROR loading file: {e}")
        return None

    # Print shape
    print(f"Dataset shape: {df.shape} - That's {df.shape[0]} rows and {df.shape[1]} columns!")

    # Print column names
    print(f"Columns: {list(df.columns)}")

    # Print first few rows
    print("\nFirst 5 rows:")
    print(df.head())

    # Print summary statistics
    print("\nSummary statistics:")
    print(df.describe())

    # Check for missing values
    print("\nMissing values per column:")
    print(df.isnull().sum())

    print("\nData exploration complete!")

    return df


# =============================================================================
# FUNCTION 2: FILTER ENVIRONMENTAL DATA
# =============================================================================

def filter_environmental_data(df, min_temp=15, max_temp=30, quality="good"):
    """
    Filter environmental data based on temperature range and data quality.

    This function demonstrates how to apply multiple filtering conditions
    to clean and prepare environmental data for analysis.

    Args:
        df (pandas.DataFrame): Environmental data with temperature and quality columns
        min_temp (float): Minimum acceptable temperature in Celsius (default: 15)
        max_temp (float): Maximum acceptable temperature in Celsius (default: 30)
        quality (str): Required data quality level (default: "good")

    Returns:
        pandas.DataFrame: Filtered data meeting all specified conditions

    Example:
        >>> filtered_df = filter_environmental_data(readings_df, min_temp=20, max_temp=30, quality='good')
        Original data: 1000 rows
        After filtering: 247 rows (24.7% of data retained)
        Filters applied:
          - Temperature: 20.0°C to 30.0°C
          - Data quality: good
    """

    print("=" * 50)
    print("FILTERING ENVIRONMENTAL DATA")
    print("=" * 50)

    # Handle empty or None input
    if df is None or df.empty:
        print("Input DataFrame is empty or None")
        return pd.DataFrame()

    # Check for required columns
    required_columns = ['temperature_c', 'data_quality']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        print(f"Missing required columns: {missing_columns}")
        return pd.DataFrame()

    original_count = len(df)
    print(f"Original data: {original_count} rows")

    # Filter by temperature range
    temp_mask = (df['temperature_c'] >= min_temp) & (df['temperature_c'] <= max_temp)
    filtered_df = df[temp_mask]

    # Filter by data quality
    filtered_df = filtered_df[filtered_df['data_quality'] == quality]

    final_count = len(filtered_df)
    pct = (final_count / original_count * 100) if original_count > 0 else 0

    print(f"After filtering: {final_count} rows ({pct:.1f}% of data retained)")
    print(f"Filters applied:")
    print(f"  - Temperature: {float(min_temp)}°C to {float(max_temp)}°C")
    print(f"  - Data quality: {quality}")

    return filtered_df


# =============================================================================
# FUNCTION 3: CALCULATE STATION STATISTICS
# =============================================================================

def calculate_station_statistics(df):
    """
    Calculate station statistics

    This function groups temperature readings by weather station and calculates
    summary statistics (average temperature, number of readings, etc.) for each
    station.

    Args:
        df (pandas.DataFrame): Environmental readings data with 'station_id', 'temperature_c' and 'humidity_percent' columns

    Returns:
        pandas.DataFrame: Statistics for each station with columns:
            - station_id: The weather station identifier
            - avg_temperature: Average temperature for this station
            - avg_humidity: Average humidity for this station
            - reading_count: Number of readings from this station

    Example:
        >>> stats_df = calculate_station_statistics(readings_df)
        Calculating statistics for 5 unique stations...
        Statistics calculated:
          - Total readings analyzed: 1000
          - Stations with data: 5
          - Average readings per station: 200.0
    """

    print("=" * 50)
    print("CALCULATING STATION STATISTICS")
    print("=" * 50)

    # Handle empty or None input
    if df is None or df.empty:
        print("Input DataFrame is empty or None")
        return pd.DataFrame()

    # Check for required columns
    required_columns = ['station_id', 'temperature_c', 'humidity_percent']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        print(f"Missing required columns: {missing_columns}")
        return pd.DataFrame()

    n_stations = df['station_id'].nunique()
    print(f"Calculating statistics for {n_stations} unique stations...")

    # Group by station_id and calculate statistics
    grouped = df.groupby('station_id')

    avg_temperature = grouped['temperature_c'].mean().round(1)
    avg_humidity = grouped['humidity_percent'].mean().round(1)
    reading_count = grouped.size()

    # Build summary DataFrame
    summary = pd.DataFrame({
        'station_id': avg_temperature.index,
        'avg_temperature': avg_temperature.values,
        'avg_humidity': avg_humidity.values,
        'reading_count': reading_count.values
    })

    total_readings = summary['reading_count'].sum()
    avg_per_station = summary['reading_count'].mean()

    print(f"Statistics calculated:")
    print(f"  - Total readings analyzed: {total_readings}")
    print(f"  - Stations with data: {len(summary)}")
    print(f"  - Average readings per station: {avg_per_station:.1f}")

    return summary


# =============================================================================
# FUNCTION 4: JOIN STATION DATA
# =============================================================================

def join_station_data(stations_df, readings_df):
    """
    Join sensor readings with station metadata

    This function joins station information (name, location) with temperature readings.
    You'll add station details (like station name and coordinates) to each temperature reading.

    Args:
        stations_df (pandas.DataFrame): Station information with 'station_id', 'station_name',
                                       'latitude', 'longitude', etc.
        readings_df (pandas.DataFrame): Temperature readings with 'station_id', 'date',
                                       'temperature_c', etc.

    Returns:
        pandas.DataFrame: Combined dataset with readings AND station information

    Example:
        >>> joined_df = join_station_data(stations_df, readings_df)
        Joining station information with readings...
        Stations table: 5 stations
        Readings table: 1000 readings
        Joined table: 1000 rows with station details added!
    """

    print("=" * 50)
    print("JOINING STATION DATA")
    print("=" * 50)

    # Handle empty or None readings
    if readings_df is None or readings_df.empty:
        print("Readings DataFrame is empty or None")
        return pd.DataFrame()

    # Handle empty or None stations
    if stations_df is None or stations_df.empty:
        print("Stations DataFrame is empty or None")
        return pd.DataFrame()

    print(f"Stations table: {len(stations_df)} stations")
    print(f"Readings table: {len(readings_df)} readings")

    # Perform left join keeping all readings
    result = pd.merge(readings_df, stations_df, on='station_id', how='left')

    print(f"Joined table: {len(result)} rows with station details added!")

    # Show new columns added from stations
    new_cols = [c for c in result.columns if c not in readings_df.columns]
    print(f"New columns added: {new_cols}")

    return result


# =============================================================================
# HELPER FUNCTIONS (You don't need to modify these - they're provided!)
# =============================================================================

def _check_required_columns(df, required_columns, data_name="DataFrame"):
    """
    Helper function to check if required columns exist in a DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame to check
        required_columns (list): List of required column names
        data_name (str): Name to use in error messages

    Returns:
        tuple: (bool, list) - (all_present, missing_columns)
    """
    if df is None or df.empty:
        return False, required_columns

    missing = [col for col in required_columns if col not in df.columns]
    return len(missing) == 0, missing


def _format_number(value, decimals=1):
    """
    Helper function to format numbers for display.

    Args:
        value: Number to format
        decimals (int): Number of decimal places

    Returns:
        str: Formatted number
    """
    try:
        return f"{float(value):.{decimals}f}"
    except (ValueError, TypeError):
        return str(value)
