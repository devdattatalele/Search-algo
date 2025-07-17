import streamlit as st
import os
import time
import google.generativeai as genai
from dotenv import load_dotenv

st.set_page_config(
    layout="wide", 
    page_title="Departmental Store Search",
    page_icon=""
)

from graph_search import Graph
from data.store_data import STORE_HIERARCHY, get_all_brands, build_graph_from_hierarchy

load_dotenv()

try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Error configuring Gemini API: {e}")
    st.stop()

@st.cache_data
def initialize_graph():
    graph_data = build_graph_from_hierarchy(STORE_HIERARCHY)
    return Graph(graph_data), graph_data

store_graph, graph_data = initialize_graph()
start_node = "Department Store"

def resolve_brand_with_gemini(user_input_brand, all_brands):
    try:
        all_brands_str = ", ".join(all_brands)
        prompt = f"""Given the following list of available brands in a departmental store: {all_brands_str}

The user is searching for '{user_input_brand}'. Please identify the closest matching brand from the provided list. If no clear match exists, respond with 'NONE'. 

Respond only with the matched brand name or 'NONE'."""
        response = model.generate_content(prompt)
        resolved_brand = response.text.strip()
        if resolved_brand == 'NONE' or resolved_brand not in all_brands:
            return None
        return resolved_brand
    except Exception as e:
        st.error(f"Error with Gemini API: {e}")
        return None

st.title(" Intelligent Departmental Store Product Search")
st.markdown("Search for a brand and compare BFS vs. DFS performance using AI-powered fuzzy matching.")

with st.sidebar:
    st.header("📊 About This Tool")
    st.markdown("")
    st.markdown("""
    **Features:**
    - 🤖 AI-powered fuzzy matching
    - 🔍 BFS vs DFS comparison
    - ⚡ Real-time performance metrics
    - 📈 Path visualization
    
    **How it works:**
    1. Enter a brand name (typos OK!)
    2. Gemini AI resolves your input
    3. Both algorithms search the store
    4. Compare their performance
    """)
    st.header("🏪 Store Structure")
    st.markdown("**Available Categories:**")
    for category in STORE_HIERARCHY.keys():
        st.markdown(f"• {category}")

st.subheader("🔍 Search for a Brand")
user_input = st.text_input(
    "Enter the brand you are looking for:",
    placeholder="e.g., 'ipone', 'Samsng Glxy', 'nike air', 'dior'",
    help="You can use fuzzy matching - typos and abbreviations are OK!"
)

search_button = st.button("🚀 Search Brand & Compare", type="primary")

if search_button:
    if not user_input.strip():
        st.warning("⚠️ Please enter a brand name to search for.")
    else:
        st.subheader("🔍 Search Results")
        with st.spinner("🤖 Using Gemini AI to resolve your query..."):
            all_brands = get_all_brands()
            resolved_brand = resolve_brand_with_gemini(user_input, all_brands)
        st.info(f"🤖 **Gemini AI resolved your query to:** {resolved_brand if resolved_brand else 'No clear match found'}")
        if not resolved_brand:
            st.error("❌ Could not find a clear match for your brand. Please try again with a different spelling.")
            st.markdown("**💡 Suggestions:**")
            st.markdown("- Check for typos in your input")
            st.markdown("- Try using just the brand name (e.g., 'Apple' instead of 'Apple iPhone')")
            st.markdown("- Browse available brands in the sidebar")
        else:
            if resolved_brand not in graph_data:
                st.error(f"❌ Brand '{resolved_brand}' not found in store database.")
            else:
                target_node = resolved_brand
                col1, col2 = st.columns(2)
                with col1:
                    with st.spinner("🔄 Running BFS..."):
                        bfs_path, bfs_nodes_visited, bfs_time = store_graph.bfs(start_node, target_node)
                with col2:
                    with st.spinner("🔄 Running DFS..."):
                        dfs_path, dfs_nodes_visited, dfs_time = store_graph.dfs(start_node, target_node)
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("### 🌐 Breadth-First Search (BFS)")
                    st.markdown(f"**🎯 Target Brand:** `{target_node}`")
                    if bfs_path:
                        st.markdown("**📍 Path Found:**")
                        path_display = " → ".join(bfs_path)
                        st.code(path_display, language=None)
                        st.success("✅ Brand found!")
                    else:
                        st.error("❌ Brand not found via BFS")
                    st.markdown(f"**👁️ Total Nodes Visited:** `{bfs_nodes_visited}`")
                    st.markdown(f"**⏱️ Execution Time:** `{bfs_time:.6f} seconds`")
                with col2:
                    st.markdown("### 🌊 Depth-First Search (DFS)")
                    st.markdown(f"**🎯 Target Brand:** `{target_node}`")
                    if dfs_path:
                        st.markdown("**📍 Path Found:**")
                        path_display = " → ".join(dfs_path)
                        st.code(path_display, language=None)
                        st.success("✅ Brand found!")
                    else:
                        st.error("❌ Brand not found via DFS")
                    st.markdown(f"**👁️ Total Nodes Visited:** `{dfs_nodes_visited}`")
                    st.markdown(f"**⏱️ Execution Time:** `{dfs_time:.6f} seconds`")
                

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    " Intelligent Departmental Store Search | Built with Streamlit & Gemini AI"
    "</div>", 
    unsafe_allow_html=True
) 