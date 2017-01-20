if !has('python') || exists("g:hopper_plugin_loaded")
	finish
endif

let g:hopper_plugin_loaded = 1 
let s:hopper_plugin_path   = escape(expand('<sfile>:p:h'), '\')


"--------------------------------------------------------------------------
"--- Mapping 
"--------------------------------------------------------------------------

command! Hopp call <SID>Hopper()

nnoremap <silent> <leader>h :Hopp<cr>
vnoremap <silent> <leader>h <esc>:Hopp<cr>


"--------------------------------------------------------------------------
"--- Global
"--------------------------------------------------------------------------
let g:hopper_header_file_ext = ['h', 'hpp',] 
let g:hopper_impl_file_ext   = ['cpp', 'm', 'mm',]
let g:hopper_header_folder_names = ['inc', 'include',]
let g:hopper_impl_folder_names   = ['src', 'source',]


"--------------------------------------------------------------------------
"--- Functions 
"--------------------------------------------------------------------------

function! s:Hopper()

    let path = s:hopper_plugin_path . '/hopper.py'
    execute 'silent pyfile ' . path

endfunction
 

