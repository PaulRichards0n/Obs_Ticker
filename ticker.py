import obspython as obs
import datetime

# User-defined settings
source_name = 'Ticker Label'       # Name of the text source
update_interval_ms = 10000         # Update interval in milliseconds
background_color = 0xFF0000FF      # Background color in ARGB format (Alpha, Red, Green, Blue)

# Add your ticker messages here
ticker_messages = [
    'Breaking News: OBS scripts are powerful!',
    'Weather Update: Sunny with a chance of Python!',
    'Tech Tip: Keep your software updated!',
    'Remember: Stay hydrated while streaming!'
     'Tech Tip: Keep dsd11111111your softdsdse updated!',

    
]

# Global variable to keep track of the current message index
current_message_index = 0

def update_ticker():
    global current_message_index

    # Get the text source
    text_source = obs.obs_get_source_by_name(source_name)
    if text_source is not None:
        # Prepare the next ticker message
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        next_message = f"{current_time} - {ticker_messages[current_message_index]}"
        
        # Update the text source with the next ticker message
        settings = obs.obs_data_create()
        obs.obs_data_set_string(settings, "text", next_message)
        obs.obs_source_update(text_source, settings)
        obs.obs_data_release(settings)
        obs.obs_source_release(text_source)

        # Update the message index
        current_message_index = (current_message_index + 1) % len(ticker_messages)

# Called on script load and reload
def script_load(settings):
    obs.timer_add(update_ticker, update_interval_ms)

    # Create the text source if it does not exist
    if not obs.obs_get_source_by_name(source_name):
        # Create text source with background color
        source_settings = obs.obs_data_create()
        obs.obs_data_set_bool(source_settings, "bk_color", True)
        obs.obs_data_set_int(source_settings, "bk_color", background_color)
        
        text_source = obs.obs_source_create("text_gdiplus", source_name, source_settings, None)
        obs.obs_data_release(source_settings)

        # Add source to current scene
        current_scene = obs.obs_scene_from_source(obs.obs_frontend_get_current_scene())
        scene_item = obs.obs_scene_add(current_scene, text_source)
        obs.obs_sceneitem_set_visible(scene_item, True)

        # Apply scroll filter to the text source
        filter_settings = obs.obs_data_create()
        scroll_filter = obs.obs_source_create_private("scroll_filter", "Scroll", filter_settings)
        obs.obs_source_filter_add(text_source, scroll_filter)

        obs.obs_data_release(filter_settings)
        obs.obs_source_release(scroll_filter)
        obs.obs_source_release(text_source)

def script_unload():
    obs.timer_remove(update_ticker)
