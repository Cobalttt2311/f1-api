"""
Error Message Constants for Formula 1 API
"""

class ErrorMessage:
    # Generic Errors
    INTERNAL_SERVER_ERROR = "An unexpected error occurred on the server."
    INVALID_REQUEST = "Invalid request payload or parameters."
    RESOURCE_NOT_FOUND = "Requested resource not found."
    DATABASE_CONNECTION_ERROR = "Failed to establish database connection."

    # Season Errors
    SEASON_NOT_FOUND = "Season not found for the given year."
    NO_SEASONS_AVAILABLE = "No season records found in the database."

    # Circuit Errors
    CIRCUIT_NOT_FOUND = "Circuit with the specified ID was not found."
    CIRCUIT_HISTORY_NOT_FOUND = "No historical race records found for this circuit."

    # Driver Errors
    DRIVER_NOT_FOUND = "Driver with the specified ID was not found."
    NO_DRIVERS_FOUND = "No drivers found matching the specified criteria."

    # Constructor Errors
    CONSTRUCTOR_NOT_FOUND = "Constructor with the specified ID was not found."
    NO_CONSTRUCTORS_FOUND = "No constructors found matching the specified criteria."

    # Race & Weekend Errors
    RACE_NOT_FOUND = "Race event not found for the given season and round/ID."
    STARTING_GRID_NOT_FOUND = "Official starting grid data not found for this race."
    QUALIFYING_RESULTS_NOT_FOUND = "Qualifying results not found for this race."
    SPRINT_RESULTS_NOT_FOUND = "Sprint race results not found for this race."
    PIT_STOPS_NOT_FOUND = "Pit stop data not found for this race."
    LAP_CHART_NOT_FOUND = "Lap time progression data not found for this race."

    # Standings Errors
    DRIVER_STANDINGS_NOT_FOUND = "Driver championship standings not found."
    CONSTRUCTOR_STANDINGS_NOT_FOUND = "Constructor championship standings not found."

    # Analytics Errors
    ANALYTICS_DATA_NOT_AVAILABLE = "Analytics data could not be computed for the given parameters."
