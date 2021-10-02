import spotipy
import spotipy.util as util
import lyricsgenius as lg
from time import sleep


# Get playing song from spotify
# Client ID - '9289d7d4b7c44044a1dd07098ef55680'
# Client Secret - '43134da423474123a0a8537d5889df30'

def get_song():
    # Get the current song playing
    try:
        token = util.prompt_for_user_token('david.kim.9', 'user-read-currently-playing', client_id='9289d7d4b7c44044a1dd07098ef55680',
                                           client_secret='43134da423474123a0a8537d5889df30', redirect_uri='http://localhost:8888/callback')
        sp = spotipy.Spotify(auth=token)
        current_song = sp.current_user_playing_track()
        song_name = current_song['item']['name']
        song_artist = current_song['item']['artists'][0]['name']
        return song_name, song_artist
    except:
        try:
            token = util.prompt_for_user_token('david.kim.9', 'user-read-currently-playing', client_id='9289d7d4b7c44044a1dd07098ef55680',
                                               client_secret='43134da423474123a0a8537d5889df30', redirect_uri='http://localhost:8888/callback')
            sp = spotipy.Spotify(auth=token)
            current_song = sp.current_user_playing_track()
            song_name = current_song['item']['name']
            song_artist = current_song['item']['artists'][0]['name']
            return song_name, song_artist
        except:
            return "", ""


def main():
    genius = lg.Genius('M-V4fucBQP_CYimhG7ZAl1f1UHmPqofWf3FG-0JKxDYDJ4MX61em4megFzr_AdVs',
                       skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
    while True:
        user_playback = get_song()
        user_song = user_playback[0]
        user_artist = user_playback[1]

        with open(f"song.txt", "w", encoding="utf-8") as f:
            try:
                head_song_artis = f"{user_song} - {user_artist}"
                head = f"\t\t{head_song_artis}\n\t----{'-' * len(head_song_artis)}----"
                song = head + "\n\n" + genius.search_song(user_song, user_artist).lyrics.replace(
                    "EmbedShare URLCopyEmbedCopy", "")
                f.write(song)
            except:
                f.write(f'No lyrics found for "{user_song}".')

        while True:
            try:
                user_playback_inloop = get_song()
                user_song_inloop = user_playback_inloop[0]
                user_artist_inloop = user_playback_inloop[1]
                if user_song != user_song_inloop or user_artist != user_artist_inloop:
                    break
            finally:
                sleep(0.1)


if __name__ == '__main__':
    main()
