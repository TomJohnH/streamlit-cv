import streamlit as st

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
# st.title("Hello")
# st.header("I'm Tomasz")
# st.subheader(
#     "senior product manager, insurance pricing manager, streamlit enthusiast & actuary"
# )

# # -------- image ------------------

# col1, col2, col3 = st.columns([1, 6, 1])

# with col1:
#     st.write("")

# with col2:
#     st.image("https://raw.githubusercontent.com/TomJohnH/cv/main/images/science.png")

# with col3:
#     st.write("")

# # -------- main part ------------------

# st.write("")

# st.subheader("About me")

# with st.expander("Expand to see more about me"):
#     st.write(
#         """
#     - I have a proven track record in product discovery, product delivery and product management.
#     - I am hyper-focused on user experience.
#     - I used to be an actuary, therefore data scientists and developers are \"my people\". I understand them and can freely discuss issues and challenges with them.
#     - I am not a developer. However, I have some experience in coding in various programming languages, including some niche platforms. This includes: Python, R, MS SQL, VBA, SAS and even C++.
#     - I am strategic in nature - I am always looking for new approaches that can give competitive advantage. This was a necessity in my career as a motor pricing manager and consultant.
#     """
#     )

# st.subheader("Education")

# with st.expander("Expand to see my education"):
#     st.write(
#         """
#         **2013 – 2014** | Warsaw School of Economics

#         Postgraduate studies

#         Analyst Academy – Statistical Analysis and Data Mining in Business

#         **2005 – 2010** | Adam Mickiewicz University in Poznań

#         Faculty of Mathematics and Computer Science

#         Specialization: Financial Mathematics and Actuarial Mathematics


#     """
#     )


# st.subheader("My experience")

# with st.expander("Expand to see my experience"):
#     st.write(
#         """
#         **09.2021 – present** | Allegro Pay sp. z o.o.

#         Position: Senior Product Manager/ Team Leader

#         Managing a feature team of 18 people, product manager and owner role - product design and delivery with a strong emphasis on customer needs. Responsible for Allegro Care.

#         **01.2019 – 09.2021** | PKO Towarzystwo Ubezpieczeń S.A.

#         Position: Motor Pricing Team leader

#         Responsibility areas: managing motor pricing team, developing motor insurance line of business (product, tariffs), statistical modelling (various machine learning techniques), data analysis & data reporting, insights development, presenting and discussing results with CFO and Board Members.

#         **10.2017 – 12.2018** | PKO TU S.A. & PKO Życie TU S.A.

#         Position: Deputy Director of Actuarial Department

#         Responsibility areas (non-life): reserving, financial planning, capital requirement calculations including SCR, reinsurance, cooperation with Supervisor and Auditors, closing of the month calculations, data analysis, presenting and discussing results with CFO and Board Members.

#         **09.2014 – 09.2017** | Deloitte Touche Tohmatsu

#         Position: Manager - Actuarial and Insurance Solutions Department

#         Responsibilities: managing team, performing calculations, data analysis, creating methodologies and models, preparing final reports, presenting results to Clients, developing innovative approaches.

#         Project experience from Central Europe, Western Europe (France, Germany, Austria) and UK


#     """
#     )

# st.markdown(
#     ' <a href="https://www.flaticon.com/free-stickers/brain" title="brain stickers" style="font-size: 0.5rem;">Brain stickers created by Stickers - Flaticon</a>',
#     unsafe_allow_html=True,
# )
