from lecture.scraping.bugs_music.models import BugsMusic

if __name__ == '__main__':
    # 20210720
    # 16
    bugsMusic = BugsMusic(f'https://music.bugs.co.kr/chart/track/realtime/total?'
             f'chartdate={"20211007"}&charthour={"11"}')
    bugsMusic.scrap()