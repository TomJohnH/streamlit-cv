import streamlit as st
import streamlit.components.v1 as components

# https://codepen.io/Hyperplexed/pen/zYWdYoo


# ------------------------------------------------------------
#
#                  Visual settings and functions
#
# ------------------------------------------------------------


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ---------------- CSS ----------------

local_css("style.css")

# ------------------------------------------------------------
#
#                  Variables and constants
#
# ------------------------------------------------------------


# ------------------------------------------------------------
#
#                        Callbacks
#
# ------------------------------------------------------------

# ------------------------------------------------------------
#
#                        Functions
#
# ------------------------------------------------------------

# ------------------------------------------------------------
#
#                        front-end
#
# ------------------------------------------------------------


# st.subheader("I'm Tomasz")

f = open("cards.txt")

st.markdown(str(f.read()), unsafe_allow_html=True)

f.close()

# components.html("""const mouseoverEvent = new Event('mouseover');

# whateverElement.dispatchEvent(mouseoverEvent);""")
