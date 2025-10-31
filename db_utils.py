from init_db import Fon


def record_guess(session, sequence, correct):
    symbols = list(sequence)
    fons = session.query(Fon).filter(Fon.symbol.in_(symbols)).all()

    for fon in fons:
        fon.total_guesses += 1
        if correct:
            fon.correct_guesses += 1

    session.commit()
