import streamlit as st

def main():
    st.title('Streamlit App with Embedded My Google Map')
    st.write('Here is an example of embedded LDS Londonderry Map:')

    # Embedding Google Map using HTML iframe
    st.markdown("""
    <iframe src="https://www.google.com/maps/d/u/0/embed?mid=1vOVdQuXIWRVDFRnkBtXbjVlbeZ63r4o&ehbc=2E312F" width="640" height="480"></iframe>

if __name__ == "__main__":
    main()

