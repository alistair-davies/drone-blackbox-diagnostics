# Drone Blackbox Diagnostics

A Python project that analyses Betaflight blackbox telemetry logs to investigate unexpected movement in FPV drone footage.

## Background

While reviewing footage from my FPV drone, I noticed unwanted movements that reduced the smooth cinematic effect I was aiming for.

Before analysing the telemetry data, I carried out a structured troubleshooting process:

- Inspected the drone for physical damage
- Checked that the DJI O4 Pro camera was securely mounted
- Replaced all propellers
- Researched reported DJI O4 gyro\-related issues
- Investigated flight controller mounting

To gather additional evidence, I extracted and analysed Betaflight blackbox telemetry logs using Python.

## Why I Built This

This project was created to investigate a real\-world flight issue rather than as a programming exercise.

I wanted to understand whether the source of the problem could be identified through telemetry data and whether Python could help analyse telemetry data that would otherwise be difficult to interpret from raw log files.

## Investigation

Areas analysed include:

- Motor output statistics
- Motor eRPM statistics
- Correlation between motor eRPM values
- Comparison of motor behaviour across a flight

The goal was to determine whether unusual motor activity, gyro behaviour or flight dynamics could explain the unwanted movement visible in recorded footage.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Betaflight Blackbox Logs

## Skills Demonstrated

- Diagnostic troubleshooting
- Telemetry analysis
- CSV data processing
- Data visualisation
- Working with real\-world sensor data
- Python scripting
- Engineering problem solving
- Data exploration using Pandas

## Example Analysis

The project calculates:

- Mean motor outputs
- Median motor outputs
- eRPM summary statistics
- Correlation between motor eRPM values

Motor correlation analysis was used to investigate whether any motor was behaving significantly differently from the others during flight.

## Outcome

The telemetry analysis formed part of a structured troubleshooting process and provided additional insight into the drone's behaviour during flight.

The issue ultimately appeared to be related to flight controller mounting, and tightening the flight controller mounting bolts significantly improved the footage quality.

Regardless of the final cause, the project provided valuable experience working with real telemetry data and using Python as a diagnostic tool.

## Future Improvements

- Automatically detect the flight\-data header row
- Refactor plotting into reusable functions
- Add command\-line arguments
- Generate diagnostic reports automatically
- Add comparison plots between multiple flights
- Improve documentation

