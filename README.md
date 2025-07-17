#  Intelligent Search & BFS/DFS Comparison

A Streamlit web application that simulates a departmental store's product hierarchy and compares the performance of Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms for finding products.

## Project Description

This application creates a hierarchical graph structure representing a departmental store's organization:
- **Categories** → **Product Types** → **Brands**
- Users can search for brands using natural language input
- The system uses Google's Gemini AI for fuzzy matching and brand disambiguation
- Both BFS and DFS algorithms search for the target brand from a root node
- Results display the search path, nodes visited, and execution time for comparison

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set up Gemini API Key
1. Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Open the `.env` file
3. Replace `YOUR_GEMINI_API_KEY_HERE` with your actual API key:
   ```
   GEMINI_API_KEY="your_actual_api_key_here"
   ```

### 3. Run the Application
```bash
streamlit run app.py
```

## Usage Instructions

1. **Start the app**: Run `streamlit run app.py` in your terminal
2. **Enter a brand name**: Type in the search box (supports fuzzy matching, e.g., "ipone" for "Apple iPhone")
3. **Click "Search Brand & Compare"**: The system will:
   - Use Gemini AI to resolve your input to the closest matching brand
   - Perform both BFS and DFS searches from the store root
   - Display results side-by-side for comparison

## Purpose

This project demonstrates:
- **Graph traversal algorithms**: Practical comparison of BFS vs DFS performance
- **AI integration**: Using Gemini for natural language processing and fuzzy matching
- **Data structures**: Hierarchical organization and graph representation
- **Performance analysis**: Real-time measurement of algorithm efficiency

## Features

- 🤖 **AI-powered search**: Gemini API for intelligent brand matching
- 📊 **Algorithm comparison**: Side-by-side BFS vs DFS performance metrics
- 🎯 **Fuzzy matching**: Handle typos and variations in brand names
- ⚡ **Real-time results**: Instant search path visualization and timing
- 📱 **Responsive UI**: Clean, modern Streamlit interface 
