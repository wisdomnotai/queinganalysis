# Project Name: Solutio
# Developed by: Alawode Wisdom Olabowale
# Matric Number: 243566
# Department of Mathematics
# For: Dr. Adeniran (Elder), Department of Statistics

import math # Required for factorial calculations

# --- Fixed Model Parameters --- 
# These parameters define the core behavior of the queuing system.
# Adjust them based on observed or estimated voter arrival and service times.
averageArrivalRate = 1.0        # Average number of voters arriving per minute
                                # (e.g., 1 voter/min means 60 voters arrive per hour)
averageServiceRatePerServer = 0.2 # Average voters served per minute per booth
                                  # (e.g., 0.2 voters/min means each voter takes 1/0.2 = 5 minutes to vote)

def getInputForServerRange():
    """
    This function prompts the user for the starting number of polling booths.
    This starting point will be used to generate a list of 10 subsequent server configurations.
    """
    while True:
        try:
            # Request the initial number of servers from the user
            startServers = int(input("Enter the STARTING number of available polling booths (servers, c): "))
            if startServers <= 0:
                print("Number of servers must be a positive whole number.")
                continue
            return startServers
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def calculateQueuingMetrics(numberOfServers):
    """
    This function calculates various M/M/c queuing model metrics for a given
    number of servers, using the predefined arrival and service rates.
    It returns a dictionary containing all requested performance indicators.
    """
    # Calculate system efficiency (server utilization)
    # This indicates the proportion of time polling booths are busy.
    serverUtilization = averageArrivalRate / (numberOfServers * averageServiceRatePerServer)

    # Check for steady-state condition
    # A system is in steady state if the arrival rate is less than the total service capacity.
    # If not in steady state, queues will grow infinitely.
    if serverUtilization >= 1:
        # Return special values for an overloaded system where averages are infinite.
        return {
            "numberOfServers": numberOfServers,
            "steadyState": False,
            "serverUtilization": serverUtilization,
            "probabilityOfSystemIdle": 0.0, # System is never fully idle if overloaded
            "probabilityArrivalHasToWait": 1.0, # Every arrival will wait
            "expectedQueueLength": float('inf'),
            "averageWaitingTimeInQueue": float('inf'),
            "averageWaitingTimeInSystem": float('inf')
        }

    # --- Calculations for Steady State System (if serverUtilization < 1) ---

    # Calculate the probability of zero customers in the system (P0)
    # P0 is the chance that no voters are waiting and all booths are free.
    summationTerm = 0.0
    for k in range(numberOfServers):
        summationTerm += ((averageArrivalRate / averageServiceRatePerServer)**k) / math.factorial(k)
    # The c-server specific term for the10
    #  formula
    cTerm = ((averageArrivalRate / averageServiceRatePerServer)**numberOfServers) / \
            (math.factorial(numberOfServers) * (1 - serverUtilization))
    probabilityOfSystemIdle = 1.0 / (summationTerm + cTerm)

    # Calculate the probability that an arrival has to wait
    # This is the probability that all servers are busy when a new voter arrives.
    # It's also P(N >= c), where N is the number of customers in the system.
    numerator = ((averageArrivalRate / averageServiceRatePerServer)**numberOfServers) * probabilityOfSystemIdle
    denominator = math.factorial(numberOfServers) * (1 - serverUtilization)
    probabilityArrivalHasToWait = numerator / denominator

    # Calculate the expected queue length (Lq)
    # This is the average number of voters waiting in line, not yet being served.
    expectedQueueLength = (probabilityOfSystemIdle *
                           ((averageArrivalRate / averageServiceRatePerServer)**numberOfServers) *
                           serverUtilization) / \
                          (math.factorial(numberOfServers) * (1 - serverUtilization)**2)

    # Calculate the average waiting time in the queue (Wq)
    # This is the average time a voter spends purely waiting before reaching a booth.
    averageWaitingTimeInQueue = expectedQueueLength / averageArrivalRate

    # Calculate the average total time a voter spends in the system (Ws)
    # This is the average time from voter arrival until they finish voting and leave.
    averageWaitingTimeInSystem = averageWaitingTimeInQueue + (1 / averageServiceRatePerServer)

    # Return all calculated metrics
    return {
        "numberOfServers": numberOfServers,
        "steadyState": True,
        "serverUtilization": serverUtilization,
        "probabilityOfSystemIdle": probabilityOfSystemIdle,
        "probabilityArrivalHasToWait": probabilityArrivalHasToWait,
        "expectedQueueLength": expectedQueueLength,
        "averageWaitingTimeInQueue": averageWaitingTimeInQueue,
        "averageWaitingTimeInSystem": averageWaitingTimeInSystem
    }

def printMetrics(metrics):
    """
    This function prints the calculated queuing metrics for a single server configuration
    in a basic, readable format.
    """
    print("\n--- Results for {} Polling Booths ---".format(metrics["numberOfServers"]))

    if not metrics["steadyState"]:
        print("When the number of polling booths is {}, the system is in an OVERLOADED state.".format(metrics["numberOfServers"]))
        print("When the system is overloaded, the system efficiency is {:.2%}.".format(metrics["serverUtilization"]))
        print("When the system is overloaded, the probability that an arrival has to wait is {:.2%}.".format(metrics["probabilityArrivalHasToWait"]))
        print("When the system is overloaded, the probability of meeting the system idle is {:.2f}.".format(metrics["probabilityOfSystemIdle"]))
        print("When the system is overloaded, the expected queue length is infinite.")
        print("When the system is overloaded, the average waiting time on the queue is infinite.")
        print("When the system is overloaded, the average waiting time in the system is infinite.")
        print("The system is NOT in a steady state.")
    else:
        print("When the number of polling booths is {}, the probability that an arrival has to wait is {:.2%}.".format(
              metrics["numberOfServers"], metrics["probabilityArrivalHasToWait"]))
        print("When the number of polling booths is {}, the probability of meeting the system idle is {:.4f}.".format(
              metrics["numberOfServers"], metrics["probabilityOfSystemIdle"]))
        print("When the number of polling booths is {}, the expected queue length is {:.2f} voters.".format(
              metrics["numberOfServers"], metrics["expectedQueueLength"]))
        print("When the number of polling booths is {}, the average waiting time on the queue is {:.2f} minutes.".format(
              metrics["numberOfServers"], metrics["averageWaitingTimeInQueue"]))
        print("When the number of polling booths is {}, the average waiting time in the system is {:.2f} minutes.".format(
              metrics["numberOfServers"], metrics["averageWaitingTimeInSystem"]))
        print("When the number of polling booths is {}, the system efficiency is {:.2%}.".format(
              metrics["numberOfServers"], metrics["serverUtilization"]))
        print("The system is in a steady state.")


# --- Main Execution of Solutio ---
if __name__ == "__main__":
    # Get the user's starting number of servers for the analysis range
    startServers = getInputForServerRange()

    print("\n--- Solutio: Comprehensive Polling System Analysis ---")
    print(f"Analyzing {10} server configurations starting from {startServers} polling booths.")
    print(f"Fixed Arrival Rate (λ): {averageArrivalRate} voters/minute")
    print(f"Fixed Service Rate per Booth (μ): {averageServiceRatePerServer} voters/minute/booth")

    # Generate a list of 10 server configurations to analyze
    serverConfigurations = [startServers + i for i in range(10)]

    # Loop through each server configuration and print its metrics
    for numServers in serverConfigurations:
        metrics = calculateQueuingMetrics(numServers)
        printMetrics(metrics)

    print("\n--- Solutio: Analysis Complete ---")
    print("These results help INEC understand the impact of different polling booth configurations.")