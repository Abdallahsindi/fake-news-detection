import { useState, useRef } from 'react'
import { predictNews } from './api'
import Sidebar from './components/Sidebar'
import HeroSection from './components/HeroSection'
import AnalysisCard from './components/AnalysisCard'
import PredictionCard from './components/PredictionCard'
import FeatureCards from './components/FeatureCards'
import LoadingSpinner from './components/LoadingSpinner'
import Footer from './components/Footer'

function App() {
  const [text, setText] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [activePage, setActivePage] = useState('home')
  const [sidebarOpen, setSidebarOpen] = useState(false)
  const textareaRef = useRef(null)

  async function handleSubmit(e) {
    e.preventDefault()
    if (!text.trim()) return

    setLoading(true)
    setError('')
    setResult(null)

    try {
      const data = await predictNews(text)
      setResult(data)
    } catch (err) {
      if (err.code === 'ERR_NETWORK') {
        setError('Could not reach the backend. Make sure the API server is running on port 8000.')
      } else if (err.response?.status === 400) {
        setError(err.response.data.detail || 'Invalid input.')
      } else {
        setError('Something went wrong. Please try again.')
      }
    } finally {
      setLoading(false)
    }
  }

  function handleReset() {
    setResult(null)
    setText('')
    setTimeout(() => {
      textareaRef.current?.focus()
      textareaRef.current?.scrollIntoView({ behavior: 'smooth', block: 'center' })
    }, 100)
  }

  return (
    <div className="min-h-screen flex">
      <Sidebar
        active={activePage}
        setActive={setActivePage}
        mobileOpen={sidebarOpen}
        onClose={() => setSidebarOpen(false)}
      />

      {/* Mobile menu button */}
      <button
        onClick={() => setSidebarOpen(!sidebarOpen)}
        className="fixed top-4 left-4 z-50 md:hidden w-10 h-10 rounded-xl bg-[#0a0e2a]/90 backdrop-blur-2xl border border-white/10 flex items-center justify-center text-white"
      >
        <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
          {sidebarOpen ? (
            <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
          ) : (
            <path strokeLinecap="round" strokeLinejoin="round" d="M4 6h16M4 12h16M4 18h16" />
          )}
        </svg>
      </button>

      <main className="main-content min-h-screen">
        <div className="main-wrapper">

          {activePage === 'home' && (
            <>
              <HeroSection />

              {!result && !loading && <AnalysisCard text={text} setText={setText} onSubmit={handleSubmit} loading={loading} textareaRef={textareaRef} />}

              {loading && (
                <div className="analyzer-card">
                  <LoadingSpinner />
                </div>
              )}

              {error && (
                <div className="analyzer-card">
                  <div className="glass-card p-5 border-red-500/20 bg-red-500/5 fade-in">
                    <div className="flex items-start gap-3">
                      <span className="text-red-400 text-lg shrink-0 mt-0.5">⚠️</span>
                      <p className="text-red-300 text-sm">{error}</p>
                    </div>
                  </div>
                </div>
              )}

              {result && !loading && (
                <div className="analyzer-card">
                  <PredictionCard result={result} />
                  <div className="analyze-again-container">
                    <button onClick={handleReset} className="analyze-again-btn">
                      🔄 Analyze Another Article
                    </button>
                  </div>
                </div>
              )}

              {!result && !loading && <FeatureCards />}
            </>
          )}

          {activePage === 'about' && (
            <div className="page-section">
              <div className="about-card glass-card p-8 md:p-10 fade-in text-center">
                <div className="w-14 h-14 rounded-2xl bg-gradient-to-br from-blue-500/20 to-blue-600/10 border border-blue-500/20 flex items-center justify-center text-2xl mx-auto mb-5">
                  {'🧠'}
                </div>
                <h2 className="text-2xl font-bold text-white mb-5">About</h2>
                <p className="text-white/60 text-sm md:text-base max-w-2xl mx-auto leading-relaxed" style={{lineHeight: '1.9'}}>
                  The Fake News Detection System is an intelligent web application developed to combat online misinformation. Powered by Machine Learning, the system analyzes textual patterns in news articles using Natural Language Processing techniques and a trained Random Forest model to determine whether submitted content is likely to be fake or factual, delivering fast and reliable predictions in real time.
                </p>
              </div>
            </div>
          )}

          {activePage === 'how-it-works' && (
            <div className="page-section">
              <div className="how-it-works-card glass-card p-10 fade-in">
                <h2 className="text-2xl font-bold text-white">How It Works</h2>
                <div className="text-white/50 text-sm leading-relaxed max-w-md mx-auto space-y-4 text-left">
                  <div className="flex items-start gap-3">
                    <span className="w-6 h-6 rounded-full bg-purple-500/20 text-purple-400 text-xs flex items-center justify-center shrink-0 mt-0.5 font-bold">1</span>
                    <p>Enter a news article or headline text.</p>
                  </div>
                  <div className="flex items-start gap-3">
                    <span className="w-6 h-6 rounded-full bg-purple-500/20 text-purple-400 text-xs flex items-center justify-center shrink-0 mt-0.5 font-bold">2</span>
                    <p>TF-IDF vectorization converts text into numerical features.</p>
                  </div>
                  <div className="flex items-start gap-3">
                    <span className="w-6 h-6 rounded-full bg-purple-500/20 text-purple-400 text-xs flex items-center justify-center shrink-0 mt-0.5 font-bold">3</span>
                    <p>Random Forest model predicts the article's authenticity.</p>
                  </div>
                  <div className="flex items-start gap-3">
                    <span className="w-6 h-6 rounded-full bg-purple-500/20 text-purple-400 text-xs flex items-center justify-center shrink-0 mt-0.5 font-bold">4</span>
                    <p>Confidence score and detailed analysis are displayed.</p>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>

        <Footer />
      </main>
    </div>
  )
}

export default App
