import spotipy
import os
import spotipy.util as util
from time import sleep


# oauth_token='BQC_M530qX96RxfP91sClFFMhJQKLY5VqNEr0k6WAofn9nM7iAJBSaSlXwi0XHGfb9zGa3KE'
# redirect_uri='http://localhost:8888/callback'
# client_secret='43134da423474123a0a8537d5889df30'
# client_id='9289d7d4b7c44044a1dd07098ef55680'

token = util.prompt_for_user_token('david.kim.9', 'user-modify-playback-state', client_id='9289d7d4b7c44044a1dd07098ef55680',
                                   client_secret='43134da423474123a0a8537d5889df30', redirect_uri='http://localhost:8888/callback')
sp = spotipy.Spotify(auth=token)


def pause():
    sp.pause_playback()


def play(song=None):
    if song is None:
        sp.start_playback()
    else:
        try:
            # spotify:track:1Yk0cQdMLx5RzzFTYwmuld
            sp.start_playback(
                uris=['spotify:track:' + sp.search(song, type='track')['tracks']['items'][0]['id']])
        except:
            print('Error: Song not found')
            sleep(0.5)


def skip():
    sp.next_track()


def add(song):
    try:
        sp.add_to_queue(sp.search(song, type='track')
                        ['tracks']['items'][0]['id'])
    except:
        print('Error: Song not found')
        sleep(0.5)


def playlist(playlist):

    # spotify:playlist:18pn71gLfdDWPJ6z3Hbdiz
    id = sp.search(playlist, type='playlist')['playlists']['items'][0]['id']
    sp.start_playback()
    sleep(100)


def main():
    while True:
        os.system('cls')
        user_input = input('Enter a command: ')
        if 'play' in user_input and 'playlist' not in user_input:
            user_input = user_input.replace('play', '')
            if user_input == '':
                play()
            else:
                user_input = user_input.replace(' ', '', 1)
                play(user_input)
        elif user_input == 'pause':
            pause()
        elif user_input == 'quit':
            break
        elif user_input == 'skip':
            skip()
        elif 'add' in user_input:
            user_input = user_input.replace('add ', '')
            add(user_input)
        elif 'playlist' in user_input:
            user_input = user_input.replace('playlist ', '')
            playlist(user_input)
        else:
            print('Invalid command')
            sleep(0.5)


if __name__ == '__main__':
    main()