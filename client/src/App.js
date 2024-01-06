import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import Footer from "./components/Footer";
import Header from "./components/Header";
// import NotFound from "./components/NotFound";
// import ActivatePage from "./pages/ActivatePage";
import HomePage from "./pages/HomePage";
import BusinessesPage from "./pages/BusinessesPage";
import ProductPage from "./pages/ProductsPage";
import BusinessesPage2 from "./pages/BusinessesPage2";


const App = () => {
  return (
    <>
      <Router>
        <Header />
        <main className="py-3">
          <Routes>
            <Route path="/" element={<HomePage />} />
          </Routes>

          <Routes>
            <Route path="/businesses" element={<BusinessesPage />}></Route>
          </Routes>
          <Routes>
            <Route path="/products" element={<ProductPage />}></Route>
          </Routes>
          <Routes>
            <Route path="/aboutus" element={<BusinessesPage2 />}></Route>
          </Routes>
          <ToastContainer />
        </main>
        <Footer />
      </Router>
    </>
  );
};

export default App;
