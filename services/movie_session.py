from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
        movie_show_time: int,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> None:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: int = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    try:
        movie_session = MovieSession.objects.get(id=session_id)
    except MovieSession.DoesNotExist:
        raise ValueError(f"Movie session with id {session_id} does not exist")

    if show_time is not None:
        movie_session.show_time = show_time
    if movie_id is not None:
        movie_session.movie_id = movie_id
    if cinema_hall_id is not None:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()

    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    return MovieSession.objects.filter(id=session_id).delete()