#!/bin/bash

# Define the service name
SERVICE_NAME="virtual-sensor.service"

echo "Checking if Fictional Sensor is reporting data via Journal..."

# 1. Check if the service is even active
if ! systemctl is-active --quiet "$SERVICE_NAME"; then
    echo "ERROR: $SERVICE_NAME is not running."
    exit 1
fi

# 2. Check for new logs in the last 10 seconds
# We look for ANY output from the service in the last minute
RECENT_LOGS=$(journalctl -u "$SERVICE_NAME" --since "10 seconds ago" --quiet)

if [ -z "$RECENT_LOGS" ]; then
    echo "ERROR: No sensor data found in journal for the last 10 seconds."
    exit 1
else
    echo "SUCCESS: Sensor is reporting fresh data to the journal."
    # Optional: Print the last line of data found
    echo "Latest reading: $(echo "$RECENT_LOGS" | tail -n 1)"
    exit 0
fi