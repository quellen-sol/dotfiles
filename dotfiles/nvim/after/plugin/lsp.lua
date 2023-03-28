local lsp = require('lsp-zero').preset({
	name = 'minimal',
	set_lsp_keymaps = true,
	manage_nvim_cmp = true,
	suggest_lsp_servers = false,
})

lsp.ensure_installed({
	'tsserver',
	'eslint',
	'rust_analyzer',
})

local cmp = require("cmp")
local cmp_mappings = lsp.defaults.cmp_mappings({
	["<C-Space>"] = cmp.mapping.complete(),
})

-- (Optional) Configure lua language server for neovim
lsp.nvim_workspace()

lsp.set_preferences({
	sign_icons = {}
})

lsp.setup_nvim_cmp({
	mapping = cmp_mappings
})

lsp.setup()

vim.diagnostic.config({
  virtual_text = true
})
