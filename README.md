# Offline Reporter
A Python program that periodically checks for an internet connection and logs any downtime it detects.

When the connection is re-established it calculates how long it was down and sends a message to a Slack channel.

It's not very robust, because it relies on a single website.

Also this is my first time writing Python so it might not be up to the general standards.

To correctly configure the program you need to create a settings.py file in the root of the project and add 
the following content to it:

    slack_webhook_url = '<your-slack-webhook-url' 

To ensure the program runs after you left the shell use:

    nohup python3 offline-reporter.py &
