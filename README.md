# autocrop
utility to auto crop images (letterbox, etc)

I used this to crop series of comic book screenshots where borders were common

## usage

python convert.py <directory-containing-original-png-files> <directory-where-renamed-jpg-files-created> <basename-to-rename-upon>

## example

{code}
convert.py "c:\Users\johns\OneDrive\Pictures\Comics\infinity gauntlet" output infinity-gauntlet 

c:\Users\johns\OneDrive\Pictures\Comics\infinity gauntlet\Screenshot (95).png => output/infinity-gauntlet-296.jpeg      c:\Users\johns\OneDrive\Pictures\Comics\infinity gauntlet\Screenshot (96).png => output/infinity-gauntlet-297.jpeg      c:\Users\johns\OneDrive\Pictures\Comics\infinity gauntlet\Screenshot (97).png => output/infinity-gauntlet-298.jpeg      c:\Users\johns\OneDrive\Pictures\Comics\infinity gauntlet\Screenshot (98).png => output/infinity-gauntlet-299.jpeg      c:\Users\johns\OneDrive\Pictures\Comics\infinity gauntlet\Screenshot (99).png => output/infinity-gauntlet-300.jpeg
{code}
