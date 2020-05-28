# twitch-compiler
Scrape Twitch Clips and Stitch Them

# Python Dependencies 
- selinium
- ffmpeg-python [NOTE: NOT python-ffmpeg!!!]
- probably more ... 

# Execution 

To scrape twitch category clips, modify cat_dict in twitch_scraper.py to insert the twitch category clips link and a key for folder name.

To stitch downloaded video for each category, run vid_comp.py. You may need to modify file_names list according to your modifaction of twitch_scraper.py.  
