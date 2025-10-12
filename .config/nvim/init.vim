" ~/.config/nvim/init.vim

call plug#begin('~/.local/share/nvim/plugged')

" Treesitter
Plug 'nvim-treesitter/nvim-treesitter', { 'branch': 'main' }

" Autopairs
Plug 'windwp/nvim-autopairs'

" Org-Mode
Plug 'nvim-orgmode/orgmode'

" Catppuccin Theme
Plug 'catppuccin/nvim', { 'as': 'catppuccin' }

call plug#end()

colorscheme catppuccin
let g:catppuccin_flavour = 'macchiato'

" Setup Autopairs
lua require('nvim-autopairs').setup({})

lua << EOF
require('orgmode').setup({
  org_agenda_files = '~/orgfiles/**/*',
  org_default_notes_file = '~/orgfiles/refile.org',
})
EOF
