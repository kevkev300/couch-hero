class Api::V1::ResponsesController < Api::V1::BaseController
  def parse
    intent = intent_params
    parameters = parameter_params

    # answer_text = find_answer(intent, parameters)
    answer_text = 'this is a response'
    @response = { fulfillmentText: answer_text }

    render :response
  end

  def answer
    @response = { fulfillmentText: 'test' } if @response.nil?
    # @answer = Response.create(text: 'test')
  end

  private

  def find_answer(intent, parameters)
    case intent
    when 'affected'
      `python3 lib/assets/python/test.py "#{parameters}"`
    end
  end

  def intent_params
    params.require[:intent].permit[:displayName]
  end

  def parameter_params
    params.require[:queryResult].permit[:parameters]
  end
end
