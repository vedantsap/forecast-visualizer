import streamlit as st

st.set_page_config(layout="wide")
st.title("CS6301 - Visualizer")

def main():
    """
    Main function to render all elements
    """
    tabs = ["Home Page and Readme", "Tab 1", "Tab 2"]
    tab_home, tab_1, tab_2 = st.tabs(tabs)

    with tab_home:
        st.header("Home page and about")
        st.markdown(
            """
            Project visualizer for CS6301 - Data Science for Smart Cities, Fall 2023
            Compelted by:
                Pranav Jadhav
                Ravi Kiran Mekala
                Vedant Sapra
            """
        )
        container_body = st.container()
        col1, col2 = container_body.columns(2)

        with col1:
            st.write("50 iterations")

        with col2:
            st.write("200 iterations")


if __name__ == "__main__":
    main()