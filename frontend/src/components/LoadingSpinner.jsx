export default function LoadingSpinner() {
  return (
    <div className="flex flex-col items-center gap-4 py-12">
      <div className="spinner" />
      <div className="text-center">
        <p className="text-white/70 text-sm font-medium">Analyzing article...</p>
        <p className="text-white/30 text-xs mt-1">Running our ML model on the submitted text</p>
      </div>
    </div>
  )
}
