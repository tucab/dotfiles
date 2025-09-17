-- AstroCommunity: import any community modules here
-- We import this file in `lazy_setup.lua` before the `plugins/` folder.
-- This guarantees that the specs are processed before any user plugins.

---@type LazySpec
return {
  "AstroNvim/astrocommunity",
  { import = "astrocommunity.pack.lua" },
  { import = "astrocommunity.colorscheme.catppuccin" },
  { import = "astrocommunity.code-runner.compiler-nvim" },
  { import = "astrocommunity.diagnostics.error-lens-nvim" },
  { import = "astrocommunity.file-explorer.mini-files" },
  { import = "astrocommunity.git.nvim-tinygit" },
  { import = "astrocommunity.icon.mini-icons" },
  { import = "astrocommunity.markdown-and-latex.render-markdown-nvim" },
  { import = "astrocommunity.motion.mini-basics" },
  -- { import = "astrocommunity.pack.markdown" },
  -- { import = "astrocommunity.pack.ruby" },
  -- { import = "astrocommunity.pack.elixir-phoenix" },
  -- { import = "astrocommunity.pack.nim" },
  { import = "astrocommunity.editing-support.nvim-treesitter-endwise" },
  -- { import = "astrocommunity.lsp.nvim-java" },
  { import = "astrocommunity.completion.nvim-cmp" },
}
