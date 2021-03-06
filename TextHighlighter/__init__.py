import os
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    TextHighlighter = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "TextHighlighter",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    TextHighlighter = components.declare_component("TextHighlighter", path=build_dir)


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/__init__.py`
if not _RELEASE:
    import streamlit as st

    st.subheader("Component with constant args")
    text = st.text_input(
        label="Text",
        value="Comparison of ranitidine and lansoprazole in short-term low-dose triple therapy for Helicobacter pylori infection.",
    )



    labels = ["O"] * len(text.split())

    text = text.split()
    text[0] = f"<b>{text[0]}</b>"

    # Create an instance of our component with a constant `name` arg, and
    # print its output value.
    with st.form(key="No"):
        output = TextHighlighter(
            tokens=text + ["$break$"] + text,
            labels=labels + ["None"] + labels,
            colors={"O": "white", "POP": "LightPink", "INT": "LightGreen", "OUT": "LightSkyBlue"},
            display_names={"O": "Other", "POP": "Population", "INT": "Intervention", "OUT": "Outcome"},
        )

        submit = st.form_submit_button("Submit")
        if submit:
            st.write(output)
