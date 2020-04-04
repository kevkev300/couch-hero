class PagesController < ApplicationController
  def home
    input_text = 1

    # execute the python script, retrun has to be a string
    @variable = `python lib/assets/python/test.py "#{input_text}"`
  end
end
