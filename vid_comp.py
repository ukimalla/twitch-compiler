import ffmpeg
import os



if __name__ == "__main__":
    # Modify this list to add/remove folders video compilation
    file_names = ["counter_strike", "valorant", "cod", "minecraft", "apex", "league"]


    for cat in file_names:
        # Gettting all *.mp4 files from directory 'cs'
        print("Getting video file names form " + cat) 

        clip_names = []
        for file in os.listdir(cat):
            if file.endswith(".mp4"):
                clip_names.append(os.path.join(cat, file))

        print(str(len(clip_names)) + " found.")

        # Loading Video Files
        in_files = []
        for vid_file_path in clip_names:
            in_files.append(ffmpeg.input(vid_file_path))

        # Creating streams list to concatinate 
        streams = []
        for f in in_files:
            streams.append(f.video.filter("scale", size="hd1080"))
            streams.append(f.audio)
       
        joined = ffmpeg.concat(*streams,  v=1, a=1).node
        v_out = joined[0]
        a_out = joined[1].filter('volume', 0.8)

        out = ffmpeg.output(v_out, a_out, os.path.join(cat, "out.mp4"))
        out.run()
