# Video Processing Utility
VPU - video processing utility

This tool should be very close to an all-in-one 
video editing tool for simple tasks.

You should be able to process videos quickly.

Simple actions should only include 3 steps.

MVP @ 2024-10-03_13.44.34

1. select the file
	Browse via path finding  
or
	Drag and drop from anywhere

3. Select Function

	Simple things that apply to the whole video with no conditions,
	e.g.: with ffmpeg command:

	  Rotate 90° clockwise

   		ffmpeg -i input.mp4 -vf "transpose=1" output_Processed.mp4

    Rotate 180° clockwise
   
	 	ffmpeg -i input.mp4 -vf "transpose=2" output_Processed.mp4
   
	Flip horizontally

		ffmpeg -i input.mp4 -vf "hflip" output_Processed.mp4
   
	Flip vertically

		ffmpeg -i input.mp4 -vf "vflip" output_Processed.mp4
   
	Change aspect ratio

		ffmpeg -i input.mp4 -vf "setdar=16/9" output_Processed.mp4

4. Output

   Select where the output file will go:
   Same location as input source
   Or default location preset by the user

  Add "_Processed" as a suffix to avoid same name errors.
