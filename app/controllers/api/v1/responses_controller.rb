class Api::V1::ResponsesController < Api::V1::BaseController
  def parse
    file = JSON.parse(request.body.read)
    intent = find_intent(file)
    parameters = find_parameters(file)

    answer_text = find_answer(intent, parameters)
    # answer_text = "intent: #{intent}, parameters: #{parameters}"
    @response = { fulfillmentText: answer_text }

    render :answer
  end

  def answer
    # @response = { fulfillmentText: 'test' } if @response.nil?
    # @answer = Response.create(text: 'test')
  end

  private

  def find_answer(intent, parameters)
    case intent
    when 'How many people are infected?'
      `python3 lib/assets/python/confirmedCases.py "#{parameters["country"]}"`
    when 'trigger number 2'
      `python -m pip install mysql-connector`  
    when 'get_version'
      `python --version`
    when 'trigger_mysql'
      str = stringify(parameters["phone-number"], parameters["zip-code"], parameters["last-name"])
      `python3 lib/assets/python/request_help.py "#{str}"`
    when '1.2 Can leave'
      `python3 lib/assets/python/best_shoppingtime.py  "#{parameters["Location"]}"`
    when 'request_help'
      str = stringify(parameters["phone-number"], parameters["zip-code"], parameters["last-name"])
      `python lib/assets/python/request_help.py "#{str}"`
    end
  end

  def find_intent(file)
    file["queryResult"]["intent"]["displayName"]
  end

  def find_parameters(file)
    file["queryResult"]["parameters"]
  end

  def stringify(param1, param2, param3)
    "#{param1} ~ #{param2} ~ #{param3}"
  end
end
