# Obs_Ticker
A ticker (scrolling text) in OBS. 

This script will create a text source called "Ticker Label" if it doesn't already exist, add a scrolling filter to it, and update its content with messages from the ticker_messages list every 10 seconds (or the interval you define).

In the Script add you msg.

# Add your ticker messages here
ticker_messages = [
    'Breaking News: OBS scripts are powerful!',
    'Weather Update: Sunny with a chance of Python!',
    'Tech Tip: Keep your software updated!',
    'Remember: Stay hydrated while streaming!'


Here's how to use this script:

Save the script as a .py file.

Open OBS and go to Tools -> Scripts.

Click the + button and add your script.

The ticker should now appear in your current scene, and it will update according to the interval set in the script.

You can customize the ticker_messages list with your messages, and they will be displayed sequentially. The update_interval_ms variable determines how often the ticker updates to the next message. The ticker will also prepend the current time to each message.


Thank Paul Richardson
