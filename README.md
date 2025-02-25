# 🌍 REST Countries Interactive Data Visualization

This project leverages the [REST Countries API](https://restcountries.com/) to explore and visualize global country data. Using Python, Pandas, Seaborn, Matplotlib, and ipywidgets, the project provides interactive visualizations for better data understanding.

---

## 🚀 Features

- **Interactive Scatter Plot:** Compare population and area with region-based filtering.
- **Top Countries Visualization:** View the top N countries by population or area.
- **Log Scale Comparison:** Handles vast differences in population and area scales.
- **Dynamic Region Selection:** Instantly filter data based on continents.
- **User-friendly Interface:** Use dropdowns and sliders for seamless interaction.

---

## 📊 Visualizations

### 1. Population vs. Area Scatter Plot
- Visualizes how population correlates with the area across regions.
- Adjustable region filter with subregion color coding.
- Logarithmic scales to handle data outliers.

### 2. Top N Countries Bar Plot
- Compare the top countries by population or area.
- Adjustable number of countries (5 to 20).

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/restcountries-visualization.git
   cd restcountries-visualization
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the notebook:**
   ```bash
   jupyter notebook
   ```

---

## 🧩 Requirements

- Python 3.8+
- pandas
- matplotlib
- seaborn
- ipywidgets
- requests
- jupyter

*Install dependencies via:*
```bash
pip install pandas matplotlib seaborn ipywidgets requests jupyter
```

---

## 📂 Project Structure

```
restcountries-visualization/
├── restcountries_visualization.ipynb  # Main notebook with visualizations
├── requirements.txt                   # Dependencies
├── README.md                          # Project documentation
└── output/                            # Saved visual outputs (if any)
```

---

## 📝 Usage

- **Select a region** using the dropdown to see population vs. area scatter plots.
- **Use sliders** to view the top countries by population or area.
- **Explore insights** from the relationships between population and land area.

---

## 💡 Example Outputs

### 📈 Population vs. Area
*Interactive scatter plot comparing population and area with color-coded subregions.*

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit: `git commit -m 'Add feature'`.
4. Push to your branch: `git push origin feature-name`.
5. Open a pull request.

---

## 📢 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🌟 Acknowledgments

- Thanks to the [REST Countries API](https://restcountries.com/) for providing comprehensive country data.
- Built with ❤️ using Python, Seaborn, and interactive Jupyter widgets.

---

🌎 *Explore the world through data!* 🚀

