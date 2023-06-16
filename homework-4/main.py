from src.video import Video, PLVideo

if __name__ == '__main__':
    # Создаем два экземпляра класса
    video1 = Video('9lO06Zxhu88')  # '9lO06Zxhu88' - это id видео из ютуб
    video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')

    print(video1.video)

    assert str(video1.title) == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
    assert str(video2.title) == 'Пушкин: наше все?'
