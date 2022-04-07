mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"aniket.wattamwar17@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=true\n\
port = $8080\n\
" > ~/.streamlit/config.toml
