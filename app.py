import streamlit as st
import views.blog
import views.email
import views.linkedin_post
import views.video_script

# 1. Global Page Config (Must be here, only once)
st.set_page_config(
    page_title="Crave Marketing App",
    layout="wide"
)

# 2. Styling
st.markdown("""
<style>
    .st-key-email_btn button, .st-key-video_btn button, .st-key-blog_btn button, .st-key-linkedin_btn button {
        width: 100%;
        border-radius: 8px;
        height: 6em;
    }
    .output-box {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        background-color: #f9f9f9;
        min-height: 500px;
    }
    .main-header {
        text-align: center; 
        font-size: 3rem; 
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #FF4B4B, #FF914D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

# 3. Navigation State
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Home'

def navigate_to(page):
    st.session_state.current_page = page

# 4. Home Page
def page_home():
    st.markdown('<div class="main-header">CRAVE MARKETING APP</div>', unsafe_allow_html=True)
    st.write("")
    
    _, col1, col2, _ = st.columns([1, 2, 2, 1])
    with col1:
        if st.button("Email Writer", use_container_width=True, key="email_btn"):
            navigate_to("Email")
        if st.button("Video Script", use_container_width=True, key="video_btn"):
            navigate_to("Video")
            
    with col2:
        if st.button("Blog Creator", use_container_width=True, key="blog_btn"):
            navigate_to("Blog")
        if st.button("LinkedIn Post", use_container_width=True, key="linkedin_btn"):
            navigate_to("LinkedIn")

# 5. Router
def main():
    if st.session_state.current_page == 'Home':
        page_home()
    elif st.session_state.current_page == 'Email':
        views.email.show(navigate_to)
    elif st.session_state.current_page == 'Blog':
        views.blog.show(navigate_to)
    elif st.session_state.current_page == 'Video':
        views.video_script.show(navigate_to)
    elif st.session_state.current_page == 'LinkedIn':
        views.linkedin_post.show(navigate_to)

if __name__ == "__main__":
    main()