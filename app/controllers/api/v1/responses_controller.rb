class Api::V1::ResponsesController < Api::V1::BaseController
  def parse
    file = JSON.parse(request.body.read)
    intent = find_intent(file)
    parameters = find_parameters(file)

    # answer_text = find_answer(intent, parameters)
    answer_text = "intent: #{intent}, parameters: #{parameters}"
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
    when 'affected'
      `python3 lib/assets/python/test.py "#{parameters}"`
    end
  end

  def find_intent(file)
    file["queryResult"]["intent"]["displayName"]
  end

  def find_parameters(file)
    file["queryResult"]["parameters"]["param"]
  end
end
