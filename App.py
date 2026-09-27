import streamlit as st
import random

st.title("🎮 Welcome to the Game, Bruhh!!!!")
st.subheader("ARE U READY TO PLAY 😉")

st.write("""
RULES:
1. A number is chosen by us.
2. You have to guess the number correctly in 10 tries.
3. The number is between 1 and 100.
""")

if "secretno" not in st.session_state:
    st.session_state.secretno = random.randint(1, 100)
    st.session_state.i = 0
    st.session_state.game_over = False

userno = st.number_input(
    "Enter ur guess 🤔:",
    min_value=1,
    max_value=100,
    step=1
)

if st.button("GUESS 🎯") and not st.session_state.game_over:

    st.session_state.i += 1

    if userno > st.session_state.secretno:
        st.warning("The number is lower 📉")

    elif userno < st.session_state.secretno:
        st.warning("The number is higher 📈")

    else:
        st.success("You guessed the correct number 😉")
        st.success(
            f"You have found the number in "
            f"{st.session_state.i} times 🎉"
        )
        st.session_state.game_over = True

    if (
        st.session_state.i >= 10
        and userno != st.session_state.secretno
    ):
        st.error("You have used all the moves 😔")
        st.error(
            f"The secret number is {st.session_state.secretno}"
        )
        st.session_state.game_over = True

if st.button("🔄 PLAY AGAIN"):

    st.session_state.secretno = random.randint(1, 100)
    st.session_state.i = 0
    st.session_state.game_over = False

    st.rerun()
