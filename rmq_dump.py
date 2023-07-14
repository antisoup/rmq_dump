import pika

class QueueViewer:
    def __init__(self, host, watching_queue, count):
            self.host = host
            self.waiting_queue = watching_queue
            self.message_count = count

    def view_queue(self) -> list:
        credentials = pika.PlainCredentials('guest', 'guest')
        parameters = pika.ConnectionParameters(self.host,
                                       5672,
                                       '/',
                                       credentials)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host))
        msgs = []
        for i in range(self.message_count):
            chl = connection.channel()
            method_frame, header_frame, body = chl.basic_get(queue=self.waiting_queue)
            if method_frame:
                # print("body : ", body)
                msgs.append(body.decode())
            else:
                print("No more messages returned")
                connection.close()
                break
        return msgs

if __name__ == '__main__':
    ip = input("IP адрес RabbitMQ: ")
    queue = input("Название очереди: ")
    count = int(input("Количество сообщений: "))
    viewer = QueueViewer(ip, queue, count)
    messages = viewer.view_queue()
    with open('./dump.txt', 'w') as f:
        for message in messages:
            f.write(f'{message}\n')