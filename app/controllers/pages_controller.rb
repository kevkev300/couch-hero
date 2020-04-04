class PagesController < ApplicationController
  def home
  end

  def test
    country = "United States"
    @text = `python3 lib/assets/python/confirmedCases.py "#{country}"`
    # @text = "hi"
  end
end
