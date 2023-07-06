import sys
import json

from flask import Flask
app = Flask(__name__)

def format_rust_code(rust_code):
    formatted_code = rust_code.strip()
    return json.dumps(formatted_code)

@app.route("/api/python")
def hello_world():
    app.logger.info('testing info log')
    print('testing print log', file=sys.stderr)
    rust_code =  """
    use anchor_lang::prelude::*;
    declare_id!("Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS");
    
    #[program]
    pub mod hello_world {
        use super::*;
        pub fn hello_world(_ctx: Context<Initialize>) -> Result<()> {
            msg!("Hello world, from solana smart contract");
            Ok(())
        }
    }
    #[derive(Accounts)]
    pub struct Initialize {}

    """

    formatted_code = format_rust_code(rust_code)
    print(formatted_code)
    return formatted_code






