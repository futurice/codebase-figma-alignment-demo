import './App.css'
import {Header} from './components/header/Header'
import {Footer} from './components/footer/Footer'
import Home from './pages/home/index'

function App() {
  return (
    <div className="app">
      <Header />
      <main className="main">
        <Home />
      </main>
      <Footer />
    </div>
  )
}

export default App
