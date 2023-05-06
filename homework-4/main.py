from src.video import Video, PLVideo

if __name__ == '__main__':
    # Создаем два экземпляра класса
    video1 = Video('9lO06Zxhu88')  # '9lO06Zxhu88' - это id видео из ютуб
    print(f"id видео: {video1.video_id}")
    print(f"Название видео: {video1.title}")
    print(f"ссылка на видео:{video1.url}")
    print(f"количество просмотров: {video1.view_count}")
    print(f"количество лайков: {video1.likeCount}")

    video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    print(f"id канала: {video2.channel_id}")

    assert str(video1.title) == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
    assert str(video2.title) == 'Пушкин: наше все?'
