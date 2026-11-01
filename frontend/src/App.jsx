import { useState, useRef } from 'react'
import { predictNews } from './services/api'
import Sidebar from './components/Sidebar'
import HeroSection from './components/HeroSection'
import AnalysisCard from './components/AnalysisCard'
import PredictionCard from './components/PredictionCard'
import FeaturesSection from './components/FeaturesSection'
import LoadingSpinner from './components/LoadingSpinner'
import Footer from './components/Footer'

function App() {
  const [text, setText] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [active, setActive] = useState('home')
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
      if (err.code === 'ERR_NETWORK') { setError('The analysis service is temporarily unavailable. Please try again in a moment.') }
      else if (err.response?.status === 400) { setError(err.response.data.detail || 'Please enter more text to analyze.') }
      else { setError('Analysis failed. Please try again.') }
    } finally { setLoading(false) }
  }

  function handleReset() {
    setResult(null)
    setText('')
    setTimeout(() => {
      textareaRef.current?.focus()
      textareaRef.current?.scrollIntoView({ behavior: 'smooth', block: 'center' })
    }, 100)
  }

  const showHome = active === 'home'
  const showAnalysis = showHome && !result && !loading
  const showLoading = showHome && loading
  const showError = showHome && error
  const showResult = showHome && result && !loading
  const showFeatures = showHome && !result && !loading

  return (
    <div className="min-h-screen">
      <Sidebar active={active} setActive={setActive} mobileOpen={sidebarOpen} onClose={() => setSidebarOpen(false)} />

      <button
        onClick={() => setSidebarOpen(true)}
        className="fixed top-4 left-4 z-50 md:hidden w-10 h-10 rounded-xl bg-[rgba(8,15,35,0.85)] backdrop-blur-xl border border-blue-500/20 flex items-center justify-center text-white cursor-pointer"
      >
        <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
          <path strokeLinecap="round" strokeLinejoin="round" d="M4 6h16M4 12h16M4 18h16" />
        </svg>
      </button>

      <main className="ml-[240px] min-h-screen flex justify-center">
        <div className="w-full max-w-7xl flex flex-col items-center px-8 py-12">
          {showHome && (
            <>
              <HeroSection />

              {showAnalysis && (
                <section className="w-full flex justify-center mt-16">
                  <AnalysisCard
                    text={text} setText={setText} onSubmit={handleSubmit}
                    loading={loading} textareaRef={textareaRef}
                    error={error} onDismissError={() => setError('')}
                  />
                </section>
              )}

              {showLoading && <LoadingSpinner />}

              {showResult && (
                <section className="w-full flex justify-center mt-16">
                  <div className="max-w-4xl w-full space-y-8">
                    <PredictionCard result={result} />
                    <div className="flex justify-center">
                      <button onClick={handleReset} className="btn-primary">🔄 Analyze Another Article</button>
                    </div>
                  </div>
                </section>
              )}

              {showFeatures && (
                <section className="w-full mt-28">
                  <FeaturesSection />
                </section>
              )}
            </>
          )}

          {active === 'about' && (
            <section className="min-h-[70vh] flex items-center justify-center w-full">
              <div className="glass-card p-10 text-center max-w-3xl w-full">
                <div className="w-14 h-14 rounded-2xl bg-gradient-to-br from-blue-500/20 to-blue-600/10 border border-blue-500/20 flex items-center justify-center text-2xl mx-auto mb-5">{'🧠'}</div>
                <h2 className="text-2xl font-bold text-white mb-4">About</h2>
                <p className="text-gray-400 text-sm sm:text-base leading-relaxed max-w-[650px] mx-auto" style={{lineHeight: '1.9'}}>
                  The Fake News Detection System is an intelligent web application developed to combat online misinformation. Powered by Machine Learning, the system analyzes textual patterns in news articles using Natural Language Processing techniques and a trained Random Forest model to determine whether submitted content is likely to be fake or factual, delivering fast and reliable predictions in real time.
                </p>
              </div>
            </section>
          )}

          {active === 'how-it-works' && (
            <section className="min-h-[70vh] flex items-center justify-center w-full">
              <div className="glass-card p-10 max-w-3xl w-full text-center">
                <h2 className="text-2xl font-bold text-white mb-8">How It Works</h2>
                <div className="max-w-lg mx-auto space-y-6 text-left">
                  {['Enter a news article or headline text.', 'TF-IDF vectorization converts text into numerical features.', 'Random Forest model predicts the article authenticity.', 'Confidence score and detailed analysis are displayed.'].map((step, i) => (
                    <div key={i} className="flex items-center gap-5">
                      <span className="w-10 h-10 rounded-full bg-blue-500/20 text-blue-400 text-sm flex items-center justify-center shrink-0 font-bold">{i + 1}</span>
                      <p className="text-gray-400 text-sm leading-relaxed">{step}</p>
                    </div>
                  ))}
                </div>
              </div>
            </section>
          )}

          <Footer />
        </div>
      </main>
    </div>
  )
}

export default App
