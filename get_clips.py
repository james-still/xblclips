import xbox
import urllib.request

xbox.client.authenticate(login='some@email.com', password='secure')
gt = xbox.GamerProfile.from_gamertag('Major Nelson')
i = 0

for clip in list(gt.clips()):
    i += 1
    urllib.request.urlretrieve(clip.media_url, 'clips/recording' + str(i) + ".mp4")
    print("clip" + str(i) + " is downloaded")
