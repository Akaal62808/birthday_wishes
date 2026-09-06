import streamlit as st
import time

st.set_page_config(
    page_title="For Simmu Bhabhi Ji 🎂",
    layout="centered"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #021f12, #064e3b, #022c22);
    color: #ffd700;
    text-align: center;
}

.title {
    font-size: 42px;
    font-weight: bold;
    text-shadow: 0 0 15px #ffd700, 0 0 30px #b8860b;
    margin-top: 40px;
}

.message {
    font-size: 21px;
    line-height: 1.8;
    margin-top: 30px;
    background: rgba(255, 215, 0, 0.08);
    padding: 28px;
    border-radius: 20px;
    border: 1px solid rgba(255, 215, 0, 0.25);
    box-shadow: 0 0 20px rgba(255, 215, 0, 0.25);
}

.stButton>button {
    background: #ffd700;
    color: #064e3b;
    border-radius: 30px;
    font-size: 18px;
    font-weight: bold;
    padding: 10px 25px;
    border: none;
    box-shadow: 0 0 15px #ffd700;
}

.stButton>button:hover {
    box-shadow: 0 0 30px #ffd700;
    transform: scale(1.03);
}

</style>
""", unsafe_allow_html=True)


# ---------------- Session Setup ----------------
if "page" not in st.session_state:
    st.session_state.page = 1

if "animation_done" not in st.session_state:
    st.session_state.animation_done = False


# ---------------- Typewriter Effect ----------------
def typewriter(text):
    placeholder = st.empty()
    typed = ""

    for char in text:
        typed += char

        placeholder.markdown(
            '<div class="message">' + typed + '</div>',
            unsafe_allow_html=True
        )

        time.sleep(0.02)


# =====================================================
# PAGE 1 - PASSWORD
# =====================================================

if st.session_state.page == 1:

    st.markdown(
        '<div class="title">🔐 A Small Surprise 🎁</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="message">'
        '🎂 Something Special For Simmu Bhabhi Ji 🌸'
        '</div>',
        unsafe_allow_html=True
    )

    password = st.text_input(
        "Enter Password",
        type="password"
    )

    if st.button("Open 🎁"):

        if password == "Guri@780":

            st.session_state.page = 2
            st.session_state.animation_done = False
            st.rerun()

        else:

            st.error("Wrong Password ❌ Try Again")


# =====================================================
# PAGE 2 - BIRTHDAY WISH
# =====================================================

elif st.session_state.page == 2:

    st.markdown(
        '<div class="title">🎂 Happy Birthday 🎂</div>',
        unsafe_allow_html=True
    )

    birthday_text = """🎉 Happy Birthday Simmu Bhabhi Ji 🎉

Wishing you a very Happy Birthday! 🌸🎂

May your life always be filled with
happiness, peace, love and countless
beautiful moments. ✨

May every new day bring you new reasons
to smile and every dream of yours
come true. 🌟

Stay happy, stay healthy,
and always keep smiling 😊💐
"""

    if not st.session_state.animation_done:

        typewriter(birthday_text)

        st.session_state.animation_done = True

    else:

        st.markdown(
            '<div class="message">' + birthday_text + '</div>',
            unsafe_allow_html=True
        )

    if st.button("Next ⏭️"):

        st.session_state.page = 3
        st.session_state.animation_done = False
        st.rerun()


# =====================================================
# PAGE 3 - SPECIAL WISHES
# =====================================================

elif st.session_state.page == 3:

    st.markdown(
        '<div class="title">🌸 Special Wishes 🌸</div>',
        unsafe_allow_html=True
    )

    special_text = """Simmu Bhabhi Ji 💐

On your special day, I just want to wish you
lots of happiness, good health and success. ❤️

May you always be surrounded by people
who care about you and bring positivity
into your life. 🌷

May this new year of your life be
more beautiful than the previous one,
filled with wonderful memories,
new opportunities and peaceful moments. ✨

Keep smiling and keep shining! 🌟😊
"""

    if not st.session_state.animation_done:

        typewriter(special_text)

        st.session_state.animation_done = True

    else:

        st.markdown(
            '<div class="message">' + special_text + '</div>',
            unsafe_allow_html=True
        )

    if st.button("Next Page ⏭️"):

        st.session_state.page = 4
        st.session_state.animation_done = False
        st.rerun()


# =====================================================
# PAGE 4 - DON'T TAKE TENSION
# =====================================================

elif st.session_state.page == 4:

    st.markdown(
        '<div class="title">🤗 One Little Reminder</div>',
        unsafe_allow_html=True
    )

    tension_text = """Simmu Bhabhi Ji 🌸

Life vich kade-kade problems aa jandiyan ne,
par ohna karke zyada tension nahi leni. ❤️

Jo vi problem hove, thoda patience rakho...
kyunki end vich sab kuch theek ho hi janda hai. ✨

Te je kade tuhanu koi problem lage,
koi tension hove, ya dil vich kujh hove,
tusi mere naal share kar sakde ho. 🤗

Har problem da solution zaroor hunda hai,
bas thoda time te positive rehna zaroori hai. 🌷

So tension nahi leni,
smile karde rehna 😊
Everything will be okay. ❤️
"""

    if not st.session_state.animation_done:

        typewriter(tension_text)

        st.session_state.animation_done = True

    else:

        st.markdown(
            '<div class="message">' + tension_text + '</div>',
            unsafe_allow_html=True
        )

    if st.button("Next ⏭️"):

        st.session_state.page = 5
        st.session_state.animation_done = False
        st.rerun()


# =====================================================
# PAGE 5 - BLESSINGS
# =====================================================

elif st.session_state.page == 5:

    st.markdown(
        '<div class="title">✨ Best Wishes ✨</div>',
        unsafe_allow_html=True
    )

    blessings_text = """May this birthday bring a beautiful
new beginning to your life. 🌸

May you always have the strength
to face every challenge,
the courage to follow your dreams,
and the happiness you truly deserve. ❤️

May every coming year bring you
more success, peace and beautiful memories. ✨

Keep believing in yourself,
keep smiling and keep spreading happiness. 😊🌷
"""

    if not st.session_state.animation_done:

        typewriter(blessings_text)

        st.session_state.animation_done = True

    else:

        st.markdown(
            '<div class="message">' + blessings_text + '</div>',
            unsafe_allow_html=True
        )

    if st.button("Final Surprise 🎁"):

        st.session_state.page = 6
        st.session_state.animation_done = False
        st.rerun()


# =====================================================
# PAGE 6 - FINAL
# =====================================================

elif st.session_state.page == 6:

    st.markdown(
        '<div class="title">🎉 Once Again 🎉</div>',
        unsafe_allow_html=True
    )

    final_text = """🎂 HAPPY BIRTHDAY SIMMU BHABHI JI 🎂

May your smile always stay the same,
your heart always stay happy,
and your life always be filled
with beautiful moments. 🌸❤️

May all your wishes come true,
all your dreams become reality,
and every new chapter of your life
bring something wonderful. ✨

Never let the little problems of life
take away your happiness.

Stay positive,
keep smiling,
and always remember...

🌟 Everything will be okay. 🌟

Have a beautiful,
wonderful and memorable birthday! 🎂💐

Once Again...

🎉 HAPPY BIRTHDAY SIMMU BHABHI JI 🎉

❤️🌸🎂✨
"""

    if not st.session_state.animation_done:

        typewriter(final_text)

        st.session_state.animation_done = True

    else:

        st.markdown(
            '<div class="message">' + final_text + '</div>',
            unsafe_allow_html=True
        )

    st.balloons()

    if st.button("❤️ Finish"):

        st.success("Happy Birthday Simmu Bhabhi Ji! 🎂🌸❤️")
